import numpy
from attr import attrs, attrib
from attr.validators import optional, instance_of
from pandas import Series

from ..base import BaseProcessor


@attrs
class Binary(BaseProcessor):
    source_type = Series
    result_type = Series

    fillval = attrib(default=True, validator=optional(instance_of(bool)))

    def raw_process(self, series):
        series = series.map(bool, na_action='ignore')

        if self.fillval is not None:
            series = series.fillna(self.fillval)

        return series.astype(numpy.uint8)
