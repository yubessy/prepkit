from pandas import Series
from pandas.util.testing import assert_series_equal

from prepkit.processor.unit.scale import Scale

from ..._helper import array_float


def test_process():
    processor = Scale(minlim=-1, maxlim=1)
    target = Series([-2.0, -1.0, 0.0, 1.0, 2.0])
    result = processor.process(target)
    expected = Series(array_float([-1.0, -1.0, 0.0, 1.0, 1.0]))
    assert_series_equal(result, expected)


def test_process_normalize():
    processor = Scale(normalize=True)
    target = Series([1, 2, 3])
    result = processor.process(target)
    expected = Series(array_float([0.0, 0.5, 1.0]))
    assert_series_equal(result, expected)


def test_process_standardize():
    processor = Scale(standardize=True)
    target = Series([0, 1, 2])
    result = processor.process(target)
    expected = Series(array_float([-1.0, 0.0, 1.0]))
    assert_series_equal(result, expected)
