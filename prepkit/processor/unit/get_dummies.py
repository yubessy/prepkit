import numpy
from attr import attrs, attrib
from pandas import Series, DataFrame, get_dummies

from ..._utils import is_nan
from ..base import BaseProcessor


@attrs
class GetDummies(BaseProcessor):
    source_type = Series
    result_type = DataFrame

    drop = attrib(default=numpy.nan)

    def raw_process(self, series):
        if not is_nan(self.drop):
            series = series.map(self._swap_drop_nan)

        return get_dummies(series).astype(numpy.uint8)

    def _swap_drop_nan(self, value):
        drop = self.drop
        if is_nan(value):
            return 'NAN'
        elif any(drop is x for x in (None, True, False)) and value is drop:
            return numpy.nan
        elif value == drop:
            return numpy.nan
        else:
            return value
