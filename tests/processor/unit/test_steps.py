import numpy
from pandas import Series
from pandas.util.testing import assert_series_equal

from prepkit.processor.unit.steps import Steps


def test_process():
    processor = Steps(6, 12, 18, 24)
    target = Series([0, 1, 5, 6, 7, 13, 20, 24, 25])
    result = processor.process(target)
    expected = Series([6, 6, 6, 6, 12, 18, 24, 24, numpy.nan])
    assert_series_equal(result, expected)


def test_process_over():
    processor = Steps(1, 3, over=5)
    target = Series([1, 2, 3, 4])
    result = processor.process(target)
    expected = Series([1, 3, 3, 5])
    assert_series_equal(result, expected)
