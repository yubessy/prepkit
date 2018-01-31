from attr import attrs, attrib
from attr.validators import optional, in_
from pandas import Series

from ..base import BaseProcessor


@attrs
class Fillna(BaseProcessor):
    source_type = Series
    result_type = Series

    METHODS = ('min', 'max', 'mean', 'median', 'mode')

    value = attrib(default=None)
    how = attrib(default=None, validator=optional(in_(METHODS)))

    @how.validator
    def validate_exclusive(self, attribute, value):
        if self.value is not None and value is not None:
            raise ValueError("Either 'val' or 'method' can be specified")
        if self.value is None and value is None:
            raise ValueError("Either 'val' or 'method' must be specified")

    def process(self, series):
        if self.value is not None:
            series = series.fillna(self.value)
        elif self.how is not None:
            series = self._fill_by_method(series)
        return series

    def _fill_by_method(self, series):
        if self.how == 'min':
            val = series.min()
        elif self.how == 'max':
            val = series.max()
        elif self.how == 'mean':
            val = series.mean()
        elif self.how == 'median':
            val = series.median()
        elif self.how == 'mode':
            val = series.mode()[0]
        return series.fillna(val)
