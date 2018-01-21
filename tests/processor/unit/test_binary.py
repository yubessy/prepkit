import numpy
from pandas import Series
from pandas.util.testing import assert_series_equal

from prepkit.processor.unit.binary import Binary

from ..._helper import array_uint8


def test_process():
    processor = Binary()
    target = Series([0, 1, numpy.nan])
    result = processor.process(target)
    expected = Series(array_uint8([0, 1, 1]))
    assert_series_equal(result, expected)


def test_process_fillval():
    processor = Binary(fillval=False)
    target = Series([0, 1, numpy.nan])
    result = processor.process(target)
    expected = Series(array_uint8([0, 1, 0]))
    assert_series_equal(result, expected)
