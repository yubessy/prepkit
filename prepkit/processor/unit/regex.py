import re
from collections import namedtuple

import numpy
from pandas import Series

from ..base import BaseProcessor


RegexGroup = namedtuple('Group', ['name', 'regex'])


class Regex(BaseProcessor):
    source_type = Series
    result_type = Series

    def __init__(self, *groups, default=numpy.nan):
        self.groups = [self._new_group(g) for g in groups]
        self.default = default

    def _new_group(self, g):
        if isinstance(g, RegexGroup):
            return g
        elif isinstance(g, dict):
            return RegexGroup(name=g['name'], regex=re.compile(g['regex']))
        else:
            raise ValueError("cannot convert to RegexGroup")

    def raw_process(self, series):
        return series.map(self._get_name, na_action='ignore')

    def _get_name(self, value):
        for name, regex in self.groups:
            if regex.match(value):
                return name
        return self.default
