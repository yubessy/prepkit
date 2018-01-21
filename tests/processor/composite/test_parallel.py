from pandas import Series, DataFrame
from pandas.testing import assert_frame_equal

from prepkit.processor.composite.parallel import Parallel
from prepkit.processor.unit.categorical import Categorical
from prepkit.processor.unit.numerical import Numerical

from ..._helper import array_uint8


def test_process():
    processor = Parallel(
        c=Categorical(),
        n=Numerical(normalize=False),
    )
    source = Series([0, 1, 2])
    result = processor.process(source)
    expected = DataFrame({
        'c__0': array_uint8([1, 0, 0]),
        'c__1': array_uint8([0, 1, 0]),
        'c__2': array_uint8([0, 0, 1]),
        'n': [0, 1, 2],
    })
    assert_frame_equal(result, expected)
