import numpy
from attr import attrs, attrib
from pandas import Series

from ..._utils import is_nan
from ..base import BaseProcessor


@attrs
class Isnull(BaseProcessor):
    source_type = Series
    result_type = Series

    null = attrib(default='AUTO')

    @null.validator
    def validate_null(self, attribute, value):
        if not (value == 'AUTO' or value is None or is_nan(value)):
            raise ValueError("null must be one of 'AUTO', None, numpy.nan")

    def raw_process(self, series):
        return self._isnull(series).astype(numpy.uint8)

    def _isnull(self, series):
        if self.null is None:
            return series.map(lambda x: x is None)
        elif is_nan(self.null):
            return series.map(is_nan)
        else:
            return series.isnull()
