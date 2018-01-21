import numpy
from pandas import Series, DataFrame
from pandas.util.testing import assert_frame_equal

from prepkit.processor.unit.categorical import Categorical

from ..._helper import array_uint8


def test_process():
    processor = Categorical()
    target = Series(['P', 'Q', 'R', numpy.nan])
    result = processor.process(target)
    expected = DataFrame({
        'P': array_uint8([1, 0, 0, 0]),
        'Q': array_uint8([0, 1, 0, 0]),
        'R': array_uint8([0, 0, 1, 0]),
    }, columns=['P', 'Q', 'R'])
    assert_frame_equal(result, expected)


def test_process_fillna():
    processor = Categorical(fillval='P')
    target = Series(['P', 'Q', 'R', numpy.nan])
    result = processor.process(target)
    expected = DataFrame({
        'P': array_uint8([1, 0, 0, 1]),
        'Q': array_uint8([0, 1, 0, 0]),
        'R': array_uint8([0, 0, 1, 0]),
    }, columns=['P', 'Q', 'R'])
    assert_frame_equal(result, expected)


def test_process_default():
    processor = Categorical(defaultval='P')
    target = Series(['P', 'Q', 'R', numpy.nan])
    result = processor.process(target)
    expected = DataFrame({
        'Q': array_uint8([0, 1, 0, 0]),
        'R': array_uint8([0, 0, 1, 0]),
        'NAN': array_uint8([0, 0, 0, 1]),
    }, columns=['NAN', 'Q', 'R'])
    assert_frame_equal(result, expected)
