from pandas import Series, DataFrame
from pandas.testing import assert_frame_equal, assert_series_equal

from prepkit.processor.unit.to import To


def test_process_to_series():
    processor = To(series='a')
    source = DataFrame({
        'a': [1],
        'b': [2],
        'c': [3],
    })
    result = processor.process(source)
    expected = Series([1], name='a')
    assert_series_equal(result, expected)


def test_process_to_frame():
    processor = To(frame='a')
    source = Series([1])
    result = processor.process(source)
    expected = DataFrame({'a': [1]})
    assert_frame_equal(result, expected)
