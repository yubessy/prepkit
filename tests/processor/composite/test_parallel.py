from pandas import Series, DataFrame
from pandas.testing import assert_frame_equal

from prepkit import GetDummies, Scale
from prepkit.processor.composite.parallel import Parallel

from ..._helper import array_uint8


def test_process():
    processor = Parallel(
        d=GetDummies(),
        s=Scale(),
    )
    source = Series([0, 1, 2])
    result = processor.process(source)
    expected = DataFrame({
        'd__0': array_uint8([1, 0, 0]),
        'd__1': array_uint8([0, 1, 0]),
        'd__2': array_uint8([0, 0, 1]),
        's': [0, 1, 2],
    })
    assert_frame_equal(result, expected)
