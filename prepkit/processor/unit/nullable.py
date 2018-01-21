import numpy
from attr import attrs, attrib
from pandas import Series

from ..._utils import is_nan
from ..base import BaseProcessor


@attrs
class Nullable(BaseProcessor):
    source_type = Series
    result_type = Series

    nullval = attrib(default='AUTO')

    def raw_process(self, series):
        return self._isnull(series).astype(numpy.uint8)

    def _isnull(self, series):
        if self.nullval == 'AUTO':
            return series.isnull()
        elif self.nullval is None:
            return series.map(lambda x: x is None)
        elif is_nan(self.nullval):
            return series.map(is_nan)
        else:
            return series == self.nullval
