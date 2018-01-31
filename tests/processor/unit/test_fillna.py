import numpy
from pandas import Series
from pandas.util.testing import assert_series_equal

from prepkit.processor.unit.fillna import Fillna

from ..._helper import array_float


def test_process():
    processor = Fillna(value=0)
    target = Series([1, 2, numpy.nan])
    result = processor.process(target)
    expected = Series(array_float([1.0, 2.0, 0.0]))
    assert_series_equal(result, expected)


def test_process_method():
    processor = Fillna(how='mean')
    target = Series([1, 2, numpy.nan])
    result = processor.process(target)
    expected = Series(array_float([1.0, 2.0, 1.5]))
    assert_series_equal(result, expected)
