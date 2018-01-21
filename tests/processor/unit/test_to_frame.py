from pandas import Series, DataFrame
from pandas.testing import assert_frame_equal

from prepkit.processor.unit.to_frame import ToFrame


def test_process():
    processor = ToFrame('a')
    source = Series([1])
    result = processor.process(source)
    expected = DataFrame({'a': [1]})
    assert_frame_equal(result, expected)
