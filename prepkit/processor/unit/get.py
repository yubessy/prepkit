from attr import attrs, attrib
from pandas import DataFrame, Series

from ..base import BaseProcessor


@attrs
class Get(BaseProcessor):
    source_type = DataFrame
    result_type = Series

    name = attrib(type=str)

    def raw_process(self, df):
        return df[self.name]
