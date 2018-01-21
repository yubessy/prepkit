from pandas import Series, DataFrame

from ..base import BaseProcessor


class To(BaseProcessor):

    @property
    def source_type(self):
        return DataFrame if self._series_name is not None else Series

    @property
    def result_type(self):
        return Series if self._series_name is not None else DataFrame

    def __init__(self, series=None, frame=None):
        self._validate(series, frame)
        self._series_name = series
        self._frame_name = frame

    def _validate(self, series_name, frame_name):
        if series_name is not None and frame_name is not None:
            raise ValueError("either'series' or 'frame' can be specified")

    def raw_process(self, source):
        if self._series_name is not None:
            return source[self._series_name]
        else:
            return source.to_frame(self._frame_name)
