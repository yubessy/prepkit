import numpy
from pandas import Series
from pandas.util.testing import assert_series_equal

from prepkit.processor.unit.regex import Regex


def test_process():
    processor = Regex(
        dict(name='a', regex='a+'),
        dict(name='b', regex='b+'),
    )
    target = Series(['a', 'aa', 'b', 'bb', 'c'])
    result = processor.process(target)
    expected = Series(['a', 'a', 'b', 'b', numpy.nan])
    assert_series_equal(result, expected)


def test_process_default():
    processor = Regex(
        dict(name='a', regex='a+'),
        default='x',
    )
    target = Series(['a', 'aa', 'b'])
    result = processor.process(target)
    expected = Series(['a', 'a', 'x'])
    assert_series_equal(result, expected)
