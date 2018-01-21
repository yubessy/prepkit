from pandas import DataFrame

from ..base import BaseProcessor


class Selector(BaseProcessor):
    source_type = DataFrame
    result_type = DataFrame

    def __init__(self, **kwargs):
        self._renamer = {origin: target for target, origin in kwargs.items()}

    def raw_process(self, df):
        selected = df[list(self._renamer.keys())]
        return selected.rename(lambda col: self._renamer[col], axis=1)
