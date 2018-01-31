import numpy
from pandas import Series

from ..base import BaseProcessor


class Steps(BaseProcessor):
    source_type = Series
    result_type = Series

    def __init__(self, *steps, over=numpy.nan):
        self.steps = steps
        self.over = over

    def raw_process(self, series):
        return series.map(self._get_step, na_action='ignore')

    def _get_step(self, value):
        for step in self.steps:
            if value <= step:
                return step
        return self.over
