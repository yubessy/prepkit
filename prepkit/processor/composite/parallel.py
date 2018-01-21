from pandas import Series, DataFrame

from ..base import BaseProcessor


class Parallel(BaseProcessor):
    result_type = DataFrame

    def __init__(self, colsep='__', **processors):
        typical_processor = list(processors.values())[0]
        self._validate_processors(processors, typical_processor)
        self._colsep = colsep
        self._processors = processors
        self._typical_processor = typical_processor

    def _validate_processors(self, processors, typical_processor):
        for p in processors.values():
            if not isinstance(p, BaseProcessor):
                raise TypeError("{} is not a processor".format(type(p)))

        for p in processors.values():
            if not p.source_type == typical_processor.source_type:
                raise TypeError("source_types are not all the same")

    @property
    def source_type(self):
        return self._typical_processor.source_type

    def raw_process(self, source):
        result = DataFrame(index=source.index)
        sep = self._colsep
        for name, p in self._processors.items():
            r = p.process(source)
            if isinstance(r, Series):
                r.name = name if not r.name else sep.join((name, r.name))
            elif isinstance(r, DataFrame):
                r = r.rename(lambda col: sep.join((name, col)), axis=1)
            else:
                raise TypeError("result is not a Series or DataFrame")
            result = result.join(r)

        return result
