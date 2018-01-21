from pandas import Series, DataFrame
from pandas.testing import assert_series_equal

from prepkit.processor.unit.get import Get


def test_process():
    processor = Get('a')
    source = DataFrame({'a': [1]})
    result = processor.process(source)
    expected = Series([1], name='a')
    assert_series_equal(result, expected)
