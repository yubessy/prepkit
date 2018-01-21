import numpy
from pandas import Series
from pandas.util.testing import assert_series_equal

from prepkit.processor.unit.numerical import Numerical

from ..._helper import array_float


def test_process():
    processor = Numerical()
    target = Series([1, 3, numpy.nan])
    result = processor.process(target)
    expected = Series(array_float([0.0, 1.0, numpy.nan]))
    assert_series_equal(result, expected)


def test_process_minmax():
    processor = Numerical(minval=2.0, maxval=4.0)
    target = Series([1, 2, 3, 4, 5])
    result = processor.process(target)
    expected = Series(array_float([0.0, 0.0, 0.5, 1.0, 1.0]))
    assert_series_equal(result, expected)


def test_process_without_normalize():
    processor = Numerical(normalize=False)
    target = Series([1, 3, numpy.nan])
    result = processor.process(target)
    expected = Series(array_float([1.0, 3.0, numpy.nan]))
    assert_series_equal(result, expected)


def test_process_fillna():
    processor = Numerical(fillval=0)
    target = Series([1, 2, numpy.nan])
    result = processor.process(target)
    expected = Series(array_float([0.5, 1.0, 0.0]))
    assert_series_equal(result, expected)


def test_process_fillna_method():
    processor = Numerical(fillmethod='mean')
    target = Series([1, 2, numpy.nan])
    result = processor.process(target)
    expected = Series(array_float([0.0, 1.0, 0.5]))
    assert_series_equal(result, expected)
