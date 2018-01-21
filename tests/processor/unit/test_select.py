from pandas import DataFrame
from pandas.testing import assert_frame_equal
from pytest import raises

from prepkit.processor.unit.select import Select


def test_process():
    processor = Select('a', x='b', y='c')
    source = DataFrame({
        'a': [1],
        'b': [2],
        'c': [3],
        'd': [4],
    })
    result = processor.process(source)
    expected = DataFrame({
        'a': [1],
        'x': [2],
        'y': [3],
    })
    assert_frame_equal(result, expected)


def test_process_nonexistent_origin():
    processor = Select(x='a', y='b', z='c')
    source = DataFrame({
        'a': [1],
        'b': [2],
    })
    with raises(KeyError):
        processor.process(source)
