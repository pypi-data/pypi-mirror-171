"""
Tests that use fake data (fd) instead of the test files.
"""
import numpy as np
import pytest
from astropy import units as u
from astropy.time import Time
from astropy.wcs import WCS

from sunraster.extern.meta import Meta

from irispy import IRISMapCube, IRISMapCubeSequence, utils

##############################################################################
# IRISMapCube Fixtures
##############################################################################
data = np.array(
    [
        [[1, 2, 3, 4], [2, 4, 5, 3], [0, 1, 2, 3]],
        [[2, 4, 5, 1], [10, 5, 2, 2], [10, 3, 3, 0]],
    ]
)
data_2D = np.array([[1, 2, 3, 4], [2, 4, 5, 3]])
data_1D = np.array([1, 2])
data_4D = np.array(
    [
        [
            [[1, 2, 3, 4], [2, 4, 5, 3], [0, 1, 2, 3]],
            [[2, 4, 5, 1], [10, 5, 2, 2], [10, 3, 3, 0]],
        ],
        [
            [[1, 2, 3, 4], [2, 4, 5, 3], [0, 1, 2, 3]],
            [[2, 4, 5, 1], [10, 5, 2, 2], [10, 3, 3, 0]],
        ],
    ]
)
header = {
    "CTYPE1": "HPLN-TAN",
    "CUNIT1": "arcsec",
    "CDELT1": 0.4,
    "CRPIX1": 0,
    "CRVAL1": 0,
    "NAXIS1": 4,
    "CTYPE2": "HPLT-TAN",
    "CUNIT2": "arcsec",
    "CDELT2": 0.5,
    "CRPIX2": 0,
    "CRVAL2": 0,
    "NAXIS2": 3,
    "CTYPE3": "Time    ",
    "CUNIT3": "seconds",
    "CDELT3": 0.3,
    "CRPIX3": 0,
    "CRVAL3": 0,
    "NAXIS3": 2,
}
wcs = WCS(header=header, naxis=3)
header_2D = {
    "CTYPE1": "HPLN-TAN",
    "CUNIT1": "arcsec",
    "CDELT1": 0.4,
    "CRPIX1": 0,
    "CRVAL1": 0,
    "NAXIS1": 4,
    "CTYPE2": "HPLT-TAN",
    "CUNIT2": "arcsec",
    "CDELT2": 0.5,
    "CRPIX2": 0,
    "CRVAL2": 0,
    "NAXIS2": 3,
}
wcs_2D = WCS(header=header_2D, naxis=2)
header_4D = {
    "CTYPE1": "Time    ",
    "CUNIT1": "seconds",
    "CDELT1": 0.4,
    "CRPIX1": 0,
    "CRVAL1": 0,
    "NAXIS1": 4,
    "CTYPE2": "HPLT-TAN",
    "CUNIT2": "arcsec",
    "CDELT2": 0.5,
    "CRPIX2": 0,
    "CRVAL2": 0,
    "NAXIS2": 3,
    "CTYPE3": "Wavelength",
    "CUNIT3": "seconds",
    "CDELT3": 0.4,
    "CRPIX3": 0,
    "CRVAL3": 0,
    "NAXIS3": 2,
    "CTYPE4": "HPLN-TAN",
    "CUNIT4": "arcsec",
    "CDELT4": 0.5,
    "CRPIX4": 0,
    "CRVAL4": 0,
    "NAXIS4": 2,
}
wcs_4D = WCS(header=header_4D, naxis=4)
header_1D = {
    "CTYPE1": "Time    ",
    "CUNIT1": "seconds",
    "CDELT1": 0.4,
    "CRPIX1": 0,
    "CRVAL1": 0,
    "NAXIS1": 2,
}
wcs_1D = WCS(header=header_1D, naxis=1)
unit = utils.DN_UNIT["SJI"]
mask_cube = data >= 0
mask_4D = data_4D >= 0
uncertainty = np.sqrt(data)
uncertainty_2D = np.sqrt(data_2D)
uncertainty_1D = np.sqrt(data_1D)
uncertainty_4D = np.sqrt(data_4D)
times = Time(["2014-12-11T19:39:00.48", "2014-12-11T19:43:07.6"])
exposure_times = 2 * np.ones((2), float) * u.s
meta = Meta({"exposure time": exposure_times}, axes={"exposure time": 0}, data_shape=data.shape)
extra_coords = [("time", 0, times)]
scaled_T = True
scaled_F = False
cube = IRISMapCube(
    data,
    wcs,
    uncertainty=uncertainty,
    mask=mask_cube,
    unit=unit,
    scaled=scaled_T,
    meta=meta,
)
cube.extra_coords.add(*extra_coords[0])
cube_2D = IRISMapCube(
    data_2D,
    wcs_2D,
    uncertainty=uncertainty_2D,
    mask=mask_cube,
    unit=unit,
    scaled=scaled_T,
    meta=meta,
)
cube_2D.extra_coords.add(*extra_coords[0])
cube_1D = IRISMapCube(
    data_1D,
    wcs_1D,
    uncertainty=uncertainty_1D,
    mask=mask_cube,
    unit=unit,
    scaled=scaled_T,
    meta=meta,
)
cube_1D.extra_coords.add(*extra_coords[0])
cube_F = IRISMapCube(
    data,
    wcs,
    uncertainty=uncertainty,
    mask=mask_cube,
    unit=unit,
    scaled=scaled_F,
    meta=meta,
)
cube_F.extra_coords.add(*extra_coords[0])
cube_4D = IRISMapCube(
    data_4D,
    wcs_4D,
    uncertainty=uncertainty_4D,
    mask=mask_4D,
    unit=unit,
    scaled=scaled_T,
    meta=meta,
)
cube_4D.extra_coords.add(*extra_coords[0])
data_dust = np.array(
    [
        [[-1, 2, -3, 4], [2, -200, 5, 3], [0, 1, 2, -300]],
        [[2, -200, 5, 1], [10, -5, 2, 2], [10, -3, 3, 0]],
    ]
)
header = {
    "CTYPE1": "HPLN-TAN",
    "CUNIT1": "arcsec",
    "CDELT1": 0.4,
    "CRPIX1": 0,
    "CRVAL1": 0,
    "NAXIS1": 4,
    "CTYPE2": "HPLT-TAN",
    "CUNIT2": "arcsec",
    "CDELT2": 0.5,
    "CRPIX2": 0,
    "CRVAL2": 0,
    "NAXIS2": 3,
    "CTYPE3": "Time    ",
    "CUNIT3": "seconds",
    "CDELT3": 0.3,
    "CRPIX3": 0,
    "CRVAL3": 0,
    "NAXIS3": 2,
}
wcs = WCS(header=header, naxis=3)
unit = utils.DN_UNIT["SJI"]
mask_dust = data_dust == -200
dust_mask_expected = np.array(
    [
        [
            [True, True, True, True],
            [True, True, True, True],
            [True, True, False, False],
        ],
        [[True, True, True, False], [True, True, True, True], [True, True, True, True]],
    ]
)
uncertainty = 1
times = Time(["2014-12-11T19:39:00.48", "2014-12-11T19:43:07.6"])
exposure_times = 2 * np.ones((2), float) * u.s
extra_coords = [("time", 0, times)]
scaled_T = True
meta = Meta({"exposure time": exposure_times, "OBSID": 1}, axes={"exposure time": 0}, data_shape=data_dust.shape)
cube_dust = IRISMapCube(
    data_dust,
    wcs,
    uncertainty=uncertainty,
    mask=mask_dust,
    unit=unit,
    scaled=scaled_T,
    meta=meta,
)
cube_dust.extra_coords.add(*extra_coords[0])

##############################################################################
# IRISMapCubeSequence Fixtures
##############################################################################
cube_seq = IRISMapCube(
    data,
    wcs,
    uncertainty=uncertainty,
    mask=mask_cube,
    unit=unit,
    meta=meta,
    scaled=scaled_T,
)
cube_seq.extra_coords.add(*extra_coords[0])
cube_seq_per_s = IRISMapCube(
    data / 2,
    wcs,
    uncertainty=uncertainty,
    mask=mask_cube,
    unit=unit / u.s,
    meta=meta,
    scaled=scaled_T,
)
cube_seq_per_s.extra_coords.add(*extra_coords[0])
cube_seq_per_s_per_s = IRISMapCube(
    data / 2 / 2,
    wcs,
    uncertainty=uncertainty,
    mask=mask_cube,
    unit=unit / u.s / u.s,
    meta=meta,
    scaled=scaled_T,
)
cube_seq_per_s_per_s.extra_coords.add(*extra_coords[0])
cube_seq_s = IRISMapCube(
    data * 2,
    wcs,
    uncertainty=uncertainty,
    mask=mask_cube,
    unit=unit * u.s,
    meta=meta,
    scaled=scaled_T,
)
cube_seq_s.extra_coords.add(*extra_coords[0])
cube_seq_s_s = IRISMapCube(
    data * 2 * 2,
    wcs,
    uncertainty=uncertainty,
    mask=mask_cube,
    unit=unit * u.s * u.s,
    meta=meta,
    scaled=scaled_T,
)
cube_seq_s_s.extra_coords.add(*extra_coords[0])
sequence = IRISMapCubeSequence(data_list=[cube_seq, cube_seq], meta=meta, common_axis=0)
sequence_per_s = IRISMapCubeSequence(data_list=[cube_seq_per_s, cube_seq_per_s], meta=meta, common_axis=0)
sequence_per_s_per_s = IRISMapCubeSequence(
    data_list=[cube_seq_per_s_per_s, cube_seq_per_s_per_s], meta=meta, common_axis=0
)
sequence_s = IRISMapCubeSequence(data_list=[cube_seq_s, cube_seq_s], meta=meta, common_axis=0)
sequence_s_s = IRISMapCubeSequence(data_list=[cube_seq_s_s, cube_seq_s_s], meta=meta, common_axis=0)
seq_dust = IRISMapCubeSequence(data_list=[cube_dust, cube_dust], meta=meta, common_axis=0)

##############################################################################
# IRISMapCube Tests
##############################################################################


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (cube, data / exposure_times[0]),
        (cube_2D, data_2D / exposure_times[0]),
        (cube_1D, data_1D / exposure_times[0]),
    ],
)
def test_IRISMapCube_apply_exposure_time_correction(test_input, expected):
    np.testing.assert_array_equal(test_input.apply_exposure_time_correction().data, expected.value)


@pytest.mark.parametrize("test_input,expected", [(cube, data * exposure_times[0])])
def test_IRISMapCube_apply_exposure_time_correction_undo(test_input, expected):
    np.testing.assert_array_equal(
        test_input.apply_exposure_time_correction(undo=True, force=True).data,
        expected.value,
    )


@pytest.mark.parametrize("test_input,expected", [(cube_dust, dust_mask_expected)])
def test_IRISMapCube_apply_dust_mask(test_input, expected):
    test_input.apply_dust_mask()
    np.testing.assert_array_equal(test_input.mask, expected)
    test_input.apply_dust_mask(undo=True)
    np.testing.assert_array_equal(test_input.mask, mask_dust)


##############################################################################
# IRISMapCubeSequence Tests
##############################################################################


@pytest.mark.parametrize("test_input,expected", [(sequence, [4, 3, 4] * u.pix)])
def test_dimensions(test_input, expected):
    assert np.any(test_input.dimensions == expected)


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            sequence,
            (
                [
                    ("meta.obs.sequence",),
                    ("time", "time"),
                    ("custom:pos.helioprojective.lon", "custom:pos.helioprojective.lat"),
                    ("custom:pos.helioprojective.lon", "custom:pos.helioprojective.lat"),
                ]
            ),
        )
    ],
)
def test_array_axis_physical_types(test_input, expected):
    assert test_input.array_axis_physical_types == expected


@pytest.mark.parametrize(
    "test_input,undo,copy,force,expected",
    [
        (sequence_s_s, False, True, True, sequence_s),
        (sequence, False, True, False, sequence_per_s),
        (sequence_per_s_per_s, True, True, True, sequence_per_s),
        (sequence_per_s, True, True, False, sequence),
        (sequence_s_s, False, False, True, sequence_s),
        (sequence, False, False, False, sequence_per_s),
        (sequence_per_s_per_s, True, False, True, sequence_per_s),
        # This fails
        # (sequence_per_s, True, False, False, sequence),
    ],
)
def test_IRISMapCubeSequence_apply_exposure_time_correction(test_input, undo, copy, force, expected):
    if copy:
        output_sequence = test_input.apply_exposure_time_correction(undo=undo, copy=copy, force=force)
    else:
        test_input.apply_exposure_time_correction(undo=undo, copy=copy, force=force)
        output_sequence = test_input
    for i in range(len(output_sequence.data)):
        np.testing.assert_array_equal(output_sequence.data[i].data, expected.data[i].data)


@pytest.mark.parametrize("test_input,expected", [(seq_dust, dust_mask_expected)])
def test_IRISMapCubeSequence_apply_dust_mask(test_input, expected):
    test_input.apply_dust_mask()
    for cube_test in seq_dust.data:
        np.testing.assert_array_equal(cube_test.mask, expected)
    test_input.apply_dust_mask(undo=True)
    for cube_test in seq_dust.data:
        np.testing.assert_array_equal(cube_test.mask, mask_dust)
