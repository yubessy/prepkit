from .processor.composite.parallel import Parallel
from .processor.composite.serial import Serial
from .processor.unit.binary import Binary
from .processor.unit.categorical import Categorical
from .processor.unit.get import Get
from .processor.unit.nullable import Nullable
from .processor.unit.numerical import Numerical
from .processor.unit.select import Select
from .processor.unit.to_frame import ToFrame

__all__ = [
    'Parallel',
    'Serial',
    'Binary',
    'Categorical',
    'Get',
    'Nullable',
    'Numerical',
    'Select',
    'ToFrame',
]

PROCESSORS = {
    'parallel': Parallel,
    'serial': Serial,
    'binary': Binary,
    'categorical': Categorical,
    'get': Get,
    'nullable': Nullable,
    'numerical': Numerical,
    'select': Select,
    'to_frame': ToFrame,
}


def build(obj):
    if isinstance(obj, dict):
        if not len(obj) == 1:
            raise ValueError("obj must have only one key")

        name = list(obj.keys())[0]
        if name not in PROCESSORS:
            raise ValueError("{} is not registered".format(name))

        param = obj[name]
        if name == 'parallel':
            if not isinstance(param, dict):
                raise ValueError("parallel param must be dict")
            return Parallel.build({k: build(v) for k, v in param.items()})
        else:
            return PROCESSORS[name].build(param)

    elif isinstance(obj, tuple) or isinstance(obj, list):
        return Serial.build([build(v) for v in obj])

    else:
        raise ValueError("illegal obj type: {}".format(type(obj)))
