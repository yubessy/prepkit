from pandas import Series, DataFrame

from ..base import BaseProcessor


class ToFrame(BaseProcessor):
    source_type = Series
    result_type = DataFrame

    def __init__(self, name):
        self._name = name

    def raw_process(self, series):
        return series.to_frame(self._name)
