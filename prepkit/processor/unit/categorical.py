import numpy
from attr import attrs, attrib
from pandas import Series, DataFrame, get_dummies

from ..._utils import is_nan
from ..base import BaseProcessor


@attrs
class Categorical(BaseProcessor):
    source_type = Series
    result_type = DataFrame

    fillval = attrib(default=None)
    defaultval = attrib(default=numpy.nan)

    def raw_process(self, series):
        series = series.map(self.get_category, na_action='ignore')

        if self.fillval is not None:
            series = series.fillna(self.fillval)

        if not is_nan(self.defaultval):
            series = self._swap_default_nan(series)

        dummies = get_dummies(series).astype(numpy.uint8)
        return dummies.rename(columns=self.get_column)

    def _swap_default_nan(self, series):
        defaultval = self.defaultval

        def replacer(x):
            if is_nan(x):
                return 'NAN'
            elif defaultval in (None, True, False) and x is defaultval:
                return numpy.nan
            elif x == defaultval:
                return numpy.nan
            else:
                return x

        return series.map(replacer)

    def get_category(self, value):
        return value

    def get_column(self, category):
        return str(category)
