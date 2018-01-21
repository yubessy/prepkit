from pandas import DataFrame, Series

from ..base import BaseProcessor


class Get(BaseProcessor):
    source_type = DataFrame
    result_type = Series

    def __init__(self, name):
        self._name = name

    def raw_process(self, df):
        return df[self._name]
