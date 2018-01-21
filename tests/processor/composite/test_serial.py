from pandas import Series, DataFrame
from pandas.testing import assert_frame_equal
from pytest import raises

from prepkit.processor.composite.serial import Serial
from prepkit.processor.unit.numerical import Numerical
from prepkit.processor.unit.categorical import Categorical

from ..._helper import array_uint8


def test_process():
    processor = Serial(Numerical(normalize=False, minval=0), Categorical())
    source = Series([-1, 0, 1, 2])
    result = processor.process(source)
    expected = DataFrame({
        '0': array_uint8([1, 1, 0, 0]),
        '1': array_uint8([0, 0, 1, 0]),
        '2': array_uint8([0, 0, 0, 1]),
    })
    assert_frame_equal(result, expected)


def test_process_cannot_connect():
    with raises(TypeError):
        Serial(Categorical(), Categorical())
