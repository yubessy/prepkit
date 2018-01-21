from pandas import DataFrame
from pandas.testing import assert_frame_equal
from pytest import raises

from prepkit.processor.unit.selector import Selector


def test_process():
    processor = Selector(x='a', y='b')
    source = DataFrame({
        'a': [1],
        'b': [2],
        'c': [3],
    })
    result = processor.process(source)
    expected = DataFrame({
        'x': [1],
        'y': [2],
    })
    assert_frame_equal(result, expected)


def test_process_nonexistent_origin():
    processor = Selector(x='a', y='b', z='c')
    source = DataFrame({
        'a': [1],
        'b': [2],
    })
    with raises(KeyError):
        processor.process(source)
