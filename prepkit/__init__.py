from .processor.composite.parallel import Parallel
from .processor.composite.serial import Serial
from .processor.unit.binarize import Binarize
from .processor.unit.binary import Binary
from .processor.unit.categorical import Categorical
from .processor.unit.fillna import Fillna
from .processor.unit.get import Get
from .processor.unit.get_dummies import GetDummies
from .processor.unit.isnull import Isnull
from .processor.unit.nullable import Nullable
from .processor.unit.numerical import Numerical
from .processor.unit.regex import Regex
from .processor.unit.scale import Scale
from .processor.unit.select import Select
from .processor.unit.steps import Steps
from .processor.unit.to_frame import ToFrame

__all__ = [
    'Parallel',
    'Serial',
    'Binarize',
    'Binary',
    'Categorical',
    'Fillna',
    'Get',
    'GetDummies',
    'Isnull',
    'Nullable',
    'Numerical',
    'Regex',
    'Scale',
    'Select',
    'Steps',
    'ToFrame',
]

PROCESSORS = {
    'parallel': Parallel,
    'serial': Serial,
    'binarize': Binarize,
    'binary': Binary,
    'categorical': Categorical,
    'fillna': Fillna,
    'get': Get,
    'get_dummies': GetDummies,
    'isnull': Isnull,
    'nullable': Nullable,
    'numerical': Numerical,
    'regex': Regex,
    'scale': Scale,
    'select': Select,
    'steps': Steps,
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
