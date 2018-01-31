import numpy
from pandas import Series
from pandas.util.testing import assert_series_equal

from prepkit.processor.unit.isnull import Isnull

from ..._helper import array_uint8


def test_process():
    processor = Isnull()
    target = Series([0, '', None, numpy.nan])
    result = processor.process(target)
    expected = Series(array_uint8([0, 0, 1, 1]))
    assert_series_equal(result, expected)


def test_process_null_none():
    processor = Isnull(null=None)
    target = Series([0, '', None, numpy.nan])
    result = processor.process(target)
    expected = Series(array_uint8([0, 0, 1, 0]))
    assert_series_equal(result, expected)


def test_process_null_nan():
    processor = Isnull(null=numpy.nan)
    target = Series([0, '', None, numpy.nan])
    result = processor.process(target)
    expected = Series(array_uint8([0, 0, 0, 1]))
    assert_series_equal(result, expected)
