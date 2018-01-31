from numbers import Number

from attr import attrs, attrib
from attr.validators import optional, instance_of
from pandas import Series

from ..base import BaseProcessor


@attrs
class Scale(BaseProcessor):
    source_type = Series
    result_type = Series

    minlim = attrib(default=None, validator=optional(instance_of(Number)))
    maxlim = attrib(default=None, validator=optional(instance_of(Number)))
    normalize = attrib(default=False, validator=instance_of(bool))
    standardize = attrib(default=False, validator=instance_of(bool))

    @maxlim.validator
    def validate_minmax(self, attribute, value):
        if (
            self.minlim is not None and self.maxlim is not None
            and self.minlim > self.maxlim
        ):
            raise ValueError("minlim is greater than maxlim")

    @standardize.validator
    def validate_exclusive(self, attribute, value):
        if self.normalize is True and value is True:
            raise ValueError(
                "Either 'normalize' or 'standardize' can be applied")

    def process(self, series):
        if self.minlim is not None:
            series = self._minlim(series)
        if self.maxlim is not None:
            series = self._maxlim(series)

        if self.normalize:
            series = self._normalize(series)
        elif self.standardize:
            series = self._standardize(series)

        return series

    def _minlim(self, series):
        return series.map(lambda v: max(self.minlim, v), na_action='ignore')

    def _maxlim(self, series):
        return series.map(lambda v: min(self.maxlim, v), na_action='ignore')

    def _normalize(self, series):
        smin, smax = series.min(), series.max()
        return (series - smin) / (smax - smin)

    def _standardize(self, series):
        mean, std = series.mean(), series.std()
        return (series - mean) / std
