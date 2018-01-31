import numpy
from pandas import Series

from ..base import BaseProcessor


class Binarize(BaseProcessor):
    source_type = Series
    result_type = Series

    def raw_process(self, series):
        return series.map(bool, na_action='ignore').astype(numpy.uint8)
