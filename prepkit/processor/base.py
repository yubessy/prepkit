class BaseProcessor:
    @classmethod
    def build(cls, param):
        if isinstance(param, dict):
            return cls(**param)
        elif isinstance(param, list) or isinstance(param, tuple):
            return cls(*param)
        else:
            return cls(param)

    @property
    def source_type(self):
        raise NotImplementedError

    @property
    def result_type(self):
        raise NotImplementedError

    def raw_process(self, source):
        raise NotImplementedError

    def process(self, source):
        if not isinstance(source, self.source_type):
            raise TypeError("source type is wrong")

        source_index = source.index
        result = self.raw_process(source)

        if not isinstance(result, self.result_type):
            raise TypeError("result type is wrong")

        if not all(result.index == source_index):
            raise ValueError("index has changed")

        return result
