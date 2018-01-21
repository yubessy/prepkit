from ..base import BaseProcessor


class Serial(BaseProcessor):

    def __init__(self, *processors):
        self._validate_processors(processors)
        self._processors = processors

    def _validate_processors(self, processors):
        for p in processors:
            if not isinstance(p, BaseProcessor):
                raise TypeError("{} is not a processor".format(type(p)))

        last_result_type = processors[0].result_type
        for p in processors[1:]:
            if not issubclass(p.source_type, last_result_type):
                raise TypeError("{} is not a subclass of {}".format(
                    p.source_type, last_result_type))
            last_result_type = p.result_type

    @property
    def source_type(self):
        return self._processors[0].source_type

    @property
    def result_type(self):
        return self._processors[-1].result_type

    def raw_process(self, source):
        tmp = source
        for p in self._processors:
            tmp = p.process(tmp)
        return tmp
