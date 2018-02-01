from attr import attrs, attrib
from pandas import Series, DataFrame

from ..base import BaseProcessor


@attrs
class ToFrame(BaseProcessor):
    source_type = Series
    result_type = DataFrame

    name = attrib(type=str)

    def raw_process(self, series):
        return series.to_frame(self.name)
