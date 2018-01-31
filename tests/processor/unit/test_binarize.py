from pandas import Series
from pandas.util.testing import assert_series_equal

from prepkit.processor.unit.binarize import Binarize

from ..._helper import array_uint8


def test_process():
    processor = Binarize()
    target = Series([0.0, 0.5, 1.0])
    result = processor.process(target)
    expected = Series(array_uint8([0, 1, 1]))
    assert_series_equal(result, expected)
