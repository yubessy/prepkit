from pandas import DataFrame

from ..base import BaseProcessor


class Select(BaseProcessor):
    source_type = DataFrame
    result_type = DataFrame

    def __init__(self, *args, **kwargs):
        tuples = [(a, a) for a in args] + [(v, k) for k, v in kwargs.items()]
        self._selector = dict(tuples)

    def raw_process(self, df):
        selected = df[list(self._selector.keys())]
        return selected.rename(lambda col: self._selector[col], axis=1)
