"""
This module provides general utility functions called by code in spectrograph.
"""

import datetime
import warnings

import astropy.units as u
import numpy as np
from astropy import constants
from astropy.convolution import Box1DKernel, convolve
from astropy.modeling import fitting
from astropy.table import Table
from scipy import interpolate

from irispy.utils.constants import RADIANCE_UNIT
from irispy.utils.utils import gaussian1d_on_linear_bg, get_interpolated_effective_area

__all__ = [
    "convert_between_DN_and_photons",
    "convert_or_undo_photons_per_sec_to_radiance",
    "calculate_photons_per_sec_to_radiance_factor",
    "calculate_orbital_wavelength_variation",
    "reshape_1D_wavelength_dimensions_for_broadcast",
    "produce_obs_repr_string",
]


def convert_between_DN_and_photons(old_data_arrays, old_unit, new_unit):
    """
    Converts arrays from IRIS DN to photons or vice versa.

    In this function, an inverse time component due to exposure time
    correction is ignored during calculations but preserved in final unit.

    Parameters
    ----------
    old_data_arrays: iterable of `numpy.ndarray`
        Arrays of data to be converted.
    old_unit: `astropy.unit.Unit`
        Unit of data arrays.
    new_unit: `astropy.unit.Unit`
        Unit to convert data arrays to.

    Returns
    -------
    `list` of `numpy.ndarray`
        Data arrays converted to new_unit.
    `astropy.unit.Unit`
        Unit of new data arrays with any inverse time component preserved.
    """
    if old_unit == new_unit or old_unit == new_unit / u.s:
        new_data_arrays = [data for data in old_data_arrays]
        new_unit_time_accounted = old_unit
    else:
        # During calculations, the time component due to exposure
        # time correction, if it has been applied, is ignored.
        # Check here whether the time correction is present in the
        # original unit so that is carried through to new unit.
        if u.s not in (old_unit * u.s).decompose().bases:
            old_unit_without_time = old_unit * u.s
            new_unit_time_accounted = new_unit / u.s
        else:
            old_unit_without_time = old_unit
            new_unit_time_accounted = new_unit
        # Convert data and uncertainty to new unit.
        new_data_arrays = [(data * old_unit_without_time).to(new_unit).value for data in old_data_arrays]
    return new_data_arrays, new_unit_time_accounted


def convert_or_undo_photons_per_sec_to_radiance(
    data_quantities,
    time_obs,
    response_version,
    obs_wavelength,
    detector_type,
    spectral_dispersion_per_pixel,
    solid_angle,
    undo=False,
):
    """
    Converts data quantities from counts/s to radiance (or vice versa).

    Parameters
    ----------
    data_quantities: iterable of `astropy.units.Quantity`
        Quantities to be converted.  Must have units of counts/s or
        radiance equivalent counts, e.g. erg / cm**2 / s / sr / Angstrom.
    time_obs: an `astropy.time.Time` object, as a kwarg, valid for version > 2
        Observation times of the datapoints.
        Must be in the format of, e.g.,
        time_obs parse_time('2013-09-03', format='utime'),
        which yields 1094169600.0 seconds in value.
        The argument time_obs is ignored for versions 1 and 2.
    response_version : `int`
        Version number of effective area file to be used. Cannot be set
        simultaneously with response_file or pre_launch kwarg. Default=4.
    obs_wavelength: `astropy.units.Quantity`
        Wavelength at each element along spectral axis of data quantities.
    detector_type: `str`
        Detector type: 'FUV', 'NUV', or 'SJI'.
    spectral_dispersion_per_pixel: scalar `astropy.units.Quantity`
        spectral dispersion (wavelength width) of a pixel.
    solid_angle: scalar `astropy.units.Quantity`
        Solid angle corresponding to a pixel.
    undo: `bool`
        If False, converts counts/s to radiance.
        If True, converts radiance to counts/s.
        Default=False

    Returns
    -------
    `list` of `astropy.units.Quantity`
        Data quantities converted to radiance or counts/s
        depending on value of undo kwarg.
    """
    # Check data quantities are in the right units.
    if undo is True:
        for i, data in enumerate(data_quantities):
            if not data.unit.is_equivalent(RADIANCE_UNIT):
                raise ValueError(
                    "Invalid unit provided.  As kwarg undo=True, "
                    "unit must be equivalent to {}.  Error found for {}th element "
                    "of data_quantities. Unit: {}".format(RADIANCE_UNIT, i, data.unit)
                )
    else:
        for data in data_quantities:
            if data.unit != u.photon / u.s:
                raise ValueError(
                    "Invalid unit provided.  As kwarg undo=False, "
                    "unit must be equivalent to {}.  Error found for {}th element "
                    "of data_quantities. Unit: {}".format(u.photon / u.s, i, data.unit)
                )
    photons_per_sec_to_radiance_factor = calculate_photons_per_sec_to_radiance_factor(
        time_obs,
        response_version,
        obs_wavelength,
        detector_type,
        spectral_dispersion_per_pixel,
        solid_angle,
    )
    # Change shape of arrays so they are compatible for broadcasting
    # with data and uncertainty arrays.
    photons_per_sec_to_radiance_factor = reshape_1D_wavelength_dimensions_for_broadcast(
        photons_per_sec_to_radiance_factor, data_quantities[0].ndim
    )
    # Perform (or undo) radiometric conversion.
    if undo is True:
        new_data_quantities = [
            (data / photons_per_sec_to_radiance_factor).to(u.photon / u.s) for data in data_quantities
        ]
    else:
        new_data_quantities = [
            (data * photons_per_sec_to_radiance_factor).to(RADIANCE_UNIT) for data in data_quantities
        ]
    return new_data_quantities


def calculate_photons_per_sec_to_radiance_factor(
    time_obs,
    response_version,
    wavelength,
    detector_type,
    spectral_dispersion_per_pixel,
    solid_angle,
):
    """
    Calculates multiplicative factor that converts counts/s to radiance for
    given wavelengths.

    Parameters
    ----------
    time_obs: an `astropy.time.Time` object, as a kwarg, valid for version > 2
        Observation times of the datapoints.
        Must be in the format of, e.g.,
        time_obs=parse_time('2013-09-03', format='utime'),
        which yields 1094169600.0 seconds in value.
        The argument time_obs is ignored for versions 1 and 2.
    response_version : `int`
        Version number of effective area file to be used. Cannot be set
        simultaneously with response_file or pre_launch kwarg. Default=4.
    wavelength: `astropy.units.Quantity`
        Wavelengths for which counts/s-to-radiance factor is to be calculated
    detector_type: `str`
        Detector type: 'FUV' or 'NUV'.
    spectral_dispersion_per_pixel: scalar `astropy.units.Quantity`
        spectral dispersion (wavelength width) of a pixel.
    solid_angle: scalar `astropy.units.Quantity`
        Solid angle corresponding to a pixel.

    Returns
    -------
    `astropy.units.Quantity`
        Mutliplicative conversion factor from counts/s to radiance units
        for input wavelengths.
    """
    # Get effective area and interpolate to observed wavelength grid.
    eff_area_interp = get_interpolated_effective_area(
        time_obs, response_version, detector_type, obs_wavelength=wavelength
    )
    # Return radiometric conversed data assuming input data is in units of photons/s.
    return (
        constants.h
        * constants.c
        / wavelength
        / u.photon
        / spectral_dispersion_per_pixel
        / eff_area_interp
        / solid_angle
    )


def reshape_1D_wavelength_dimensions_for_broadcast(wavelength, n_data_dim):
    if n_data_dim == 1:
        pass
    elif n_data_dim == 2:
        wavelength = wavelength[np.newaxis, :]
    elif n_data_dim == 3:
        wavelength = wavelength[np.newaxis, np.newaxis, :]
    else:
        raise ValueError("IRISSpectrogram dimensions must be 2 or 3.")
    return wavelength


def produce_obs_repr_string(meta):
    obs_info = [meta.get(key, "Unknown") for key in ["OBSID", "OBS_DESC", "STARTOBS", "ENDOBS"]]
    return """OBS ID: {obs_id}
OBS Description: {obs_desc}
OBS period: {obs_start} -- {obs_end}""".format(
        obs_id=obs_info[0],
        obs_desc=obs_info[1],
        obs_start=obs_info[2],
        obs_end=obs_info[3],
    )


# TODO: This entire function is very broken.
def calculate_orbital_wavelength_variation(
    data_array,
    date_data_created,
    slit_pixel_range=None,
    spline_smoothing=False,
    fit_individual_profiles=False,
    spacecraft_velocity=None,
    orbital_phase=None,
    roll_angle=None,
):
    """
    Calculates orbital corrections of spectral line positions using level 2
    files.

    For data generated from the April 2014 pipeline, thermal and spacecraft velocity components
    have both been subtracted in the level 2 files. Therefore, this routine calculates the
    residual orbital (thermal) variation. For data generated from the Oct 2013 pipeline,
    this routine calculates the total of thermal and spacecraft velocity components.

    Parameters
    ----------
    data_array: `xarray.DataArray`
        IRIS spectrograph data from spectral window Mg II k 2796 as generated by
        `sunpy.spectra.sources.IRISRaster.`
    date_data_created: `datetime.datetime`
        Date the data was created by IRIS pipeline.  Used to determine where spacecraft
        velocity etc. needs to be accounted for.
    spacecraft_velocity: `astropy.units.quantity.Quantity`
        Velocity of spacecraft at each exposure in data_array.
        Must be set if date_data_created < 1 April 2014.
    orbital_phase: `numpy.array`
        Orbital phase of spacecraft at each exposure in data_array.  Available from
        auxiliary data in IRIS spectrograph fits files.
        Must be set if date_data_created < 1 April 2014.
    roll_angle: `astropy.units.quantity.Quantity`
        Roll angle of spacecraft. Must be set if date_data_created < 1 April 2014.

    Returns
    -------
    `astropy.table.Table`
        Contains the following columns:
            - time: `datetime.datetime` objects
                Observation times of wavelength variations.
            - FUV: `astropy.quantity.Quantity`
                Wavelength variation in the FUV.
            - NUV: `astropy.quantity.Quantity`
                Wavelength variation in the NUV.
    """
    # Define vacuum rest wavelength of Ni I 2799 line.
    wavelength_nii = 2799.474 * u.Angstrom
    # Define factor converting NUV spectral pixel size to Angstrom
    specsize = 0.0255
    # Define date of new pipeline.
    date_new_pipeline = datetime.datetime(2014, 4, 1)
    if date_data_created < date_new_pipeline:
        # Check that there are measurement times with good values of
        # spacecraft velocity and orbital phase.
        bad_aux = np.asarray(
            np.isfinite(spacecraft_velocity) * np.isfinite(orbital_phase) * (-1),
            dtype=bool,
        )
    # Generate wavelength vector containing only Ni I line.
    wavelength_window = u.Quantity(
        data_array.coords["wavelength"].values,
        unit=data_array.attrs["units"]["wavelength"],
    )
    wavelength_roi_index = np.arange(len(wavelength_window))[
        np.logical_and(
            wavelength_window >= 2799.3 * u.Angstrom,
            wavelength_window <= 2799.8 * u.Angstrom,
        )
    ]
    # Check that there are at least 5 points in wavelength region.
    # Must have at least this many for a gaussian fit.
    if len(wavelength_roi_index) < 5:
        wavelength_roi_index = np.arange(5) + wavelength_roi_index[0]
    # Extract wavelength of region around Ni I line as array in units
    # of Angstroms.
    wavelength_roi = wavelength_window.to(u.Angstrom).value[wavelength_roi_index]
    # Keep only data within wavelength region of interest.
    data_array = data_array.isel(spectral_axis=slice(wavelength_roi_index[0], wavelength_roi_index[-1] + 1))
    # If user selected a sub-region of the slit, reduce data to just
    # that region.
    if slit_pixel_range:
        if len(slit_pixel_range) == 2:
            data_array = data_array.isel(slit_axis, slice(slit_pixel_range[0], slit_pixel_range[1]))
        else:
            raise TypeError(
                "slit_pixel_range must be tuple of length 2 giving lower and "
                + "upper bounds of section of slit over which to average line fits."
            )

    # Derive residual orbital variation.
    # Define array to hold averaged position of Ni I line at different
    # times.
    mean_line_wavelengths = np.empty(len(data_array.time)) * np.nan
    # Define initial guess for gaussian model.
    g_init = gaussian1d_on_linear_bg(
        amplitude=-2.0,
        mean=wavelength_nii.value,
        standard_deviation=2.0,
        constant_term=50.0,
        linear_term=1.5,
    )
    # Define fitting method.
    fit_g = fitting.LevMarLSQFitter()
    # Depending on user choice, either fit line as measured by each
    # pixel then average line position, or fit average line spectrum
    # from all slit pixels.
    if fit_individual_profiles:
        pixels_in_slit = len(raster.slit_axis)
        for k in range(len(raster.time)):
            pixel_line_wavelengths = np.empty(pixels_in_slit) * np.nan
            data_single_time = raster.isel(raster_axis=k)
            # Iterate through each pixel along slit and perform fit to
            # Ni I line.
            for j in range(2, pixels_in_slit - 2):
                # Average over 5 pixels to improve signal-to-noise.
                intensity_mean_5pix = data_single_time.isel(slit_axis=slice(j - 2, j + 3)).mean(axis=0)
                # Fit gaussian to Ni I line.
                g = fit_g(g_init, wavelength_roi, intensity_mean_5pix)
                # Check that fit is within physically reasonable
                # limits.  If so, store line center wavelength in
                # mean_line_wavelengths array. Else leave element as
                # defined, i.e. NaN.
                if np.isfinite(g.amplitude) and g.amplitude < 0.0 and wavelength_roi[0] < g.mean < wavelength_roi[-1]:
                    pixel_line_wavelengths[j] = g.mean
            # Take average of Ni I line position from fits in each
            # pixel.
            mean_line_wavelengths[k] = np.nanmean(pixel_line_wavelengths)
    else:
        # Else average all line profiles then perform fit.
        # Iterate through each measurement time and fit a gaussian to
        # Ni I line.
        for k in range(len(raster.time)):
            # Get data averaged over slit.
            data_single_time = raster.isel(raster_axis=k)
            data_slit_averaged = data_single_time.to_masked_array().mean(axis=0).data
            # Fit Ni I line with a gaussian.
            # Perform fit.
            g = fit_g(g_init, wavelength_roi, data_slit_averaged)
            # Check that fit is within physically reasonable limits.
            # If so, store line center wavelength in
            # mean_line_wavelengths array. Else leave element as
            # defined, i.e. NaN.
            if np.isfinite(g.amplitude) and g.amplitude < 0.0 and wavelength_roi[0] < g.mean < wavelength_roi[-1]:
                mean_line_wavelengths[k] = g.mean
            # If data produced by old pipeline, subtract spacecraft velocity
            # from the line position.
            if date_created < date_new_pipeline:
                mean_line_wavelengths[k] = (
                    mean_line_wavelengths[k] - spacecraft_velocity[k] / 3e8 * wavelength_nii.to(u.Angstrom).value
                )

    # Mark abnormal values.  Thermal drift is of the order of 2
    # unsummed wavelength pixels peak-to-peak.
    w_abnormal = np.where(np.abs(mean_line_wavelengths - np.nanmedian(mean_line_wavelengths)) >= specsize * 2)[0]
    if len(w_abnormal) > 0:
        mean_line_wavelengths[w_abnormal] = np.nan
    # Further data reduction required for files from old pipeline.
    if date_created < date_new_pipeline:
        dw_th_A = mean_line_wavelengths - np.nanmean(mean_line_wavelengths)
        # Change the unit from Angstrom into unsummed wavelength pixel.
        dw_th_p = dw_th_A / specsize
        # Adjust reference wavelength using orbital phase information.
        if not (np.isfinite(orbital_phase)).all():
            warnings.warn("Orbital phase values are invalid.  Thermal drift may be offset by at most one pixel.")
            dw_th = dw_th
            # For absolute wavelength calibration of NUV, the
            # following amount (unit Angstrom) has to be
            # subtracted from the wavelengths.
            np.nanmean(mean_line_wavelengths) - wavelength_nii.to(u.Angstrom).value
        else:
            # Define empirical sine fitting at 0 roll angle shifted by
            # different phase.
            sine_params = [
                -0.66615146,
                -1.0,
                53.106583 - roll_angle / 360.0 * 2 * np.pi,
            ]
            phase_adj = np.nanmean(sine_params[0] * np.sin(sine_params[1] * orbital_phase + sine_params[2]))
            # thermal component of the orbital variation, in the unit of unsummed wavelength pixel
            dw_th = dw_th_p + phase_adj
            # For absolute wavelength calibration of NUV the following
            # amount (unit Angstrom) has to be subtracted from the
            # wavelengths.
            np.nanmean(mean_line_wavelengths) - wavelength_nii.to(u.Angstrom).value - phase_adj * specsize
    else:
        # Calculate relative variation of the line position.
        dw_th = mean_line_wavelengths - np.nanmean(mean_line_wavelengths)

    # If spline_smoothing=True, perform spline fit a smoothing to
    # eliminate the 5 minute photospheric oscillation.
    if spline_smoothing:
        # Define spacing of spline knots in seconds.
        spline_knot_spacing = 300.0
        # Create array of time in seconds from first time and
        # calculate duration of fitting period.
        time_s = np.asarray(x.coords["time"] - x.coords["time"][0], dtype=float) / 1e9
        duration = time_s[-1] - time_s[0]
        # Check whether there is enough good data for a spline fit.
        if duration < spline_knot_spacing:
            raise ValueError("Not enough data for spline fit.")
        # Check whether there is enough good data for a spline fit.
        wgood = np.isfinite(mean_line_wavelengths)
        ngood = float(sum(wgood))
        wbad = not (np.isfinite(mean_line_wavelengths))
        nbad = float(sum(wbad))
        if nbad / ngood > 0.25:
            raise ValueError("Not enough good data for spline fit.")
        # Smooth residual thermal variation curve to eliminate the
        # 5-min photospheric oscillation.
        # Determine number of smoothing point using 3 point
        # lagrangian derivative.
        deriv_time = np.array([(time_s[i + 1] - time_s[i - 1]) / 2.0 for i in range(1, len(time_s) - 1)])
        deriv_time = np.insert(deriv_time, 0, (-3 * time_s[0] + 4 * time_s[1] - time_s[2]) / 2)
        deriv_time = np.insert(deriv_time, -1, (3 * time_s[-1] - 4 * time_s[-2] + time_s[-3]) / 2)
        n_smooth = int(spline_knot_spacing / deriv_time.mean())
        if n_smooth < len(wgood):
            dw_good = convolve(dw_th[good], Box1DKernel(n_smooth))
        else:
            dw_good = dw_th[good]
        time_good = time_s[good]
        # Fit spline.
        tck = interpolate.splrep(time_good, dw_good, s=0)
        dw_th = interpolate.splev(time_s, tck)

    # Derive residual orbital curves in FUV and NUV and store
    # in a table.
    times = [datetime.datetime.utcfromtimestamp(t / 1e9) for t in raster.coords["time"].values.tolist()]
    # Depeding on which pipeline produced the files...
    if date_created < date_new_pipeline:
        dw_orb_fuv = dw_th * (-0.013) + spacecraft_velocity.to(u.km / u.s).value / (3.0e5) * 1370.0 * u.Angstrom
        dw_orb_nuv = dw_th * 0.0255 + spacecraft_velocity.to(u.km / u.s).value / (3.0e5) * 2800.0 * u.Angstrom
    else:
        dw_orb_fuv = dw_th * (-1) * u.Angstrom
        dw_orb_nuv = dw_th * u.Angstrom

    orbital_wavelength_variation = Table(
        [times, dw_orb_fuv, dw_orb_nuv],
        names=("time", "wavelength variation FUV", "wavelength variation NUV"),
    )
    return orbital_wavelength_variation
