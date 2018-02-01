from prepkit import build, Get, Parallel, Serial, GetDummies


def test_build():
    p = build({'get': 'a'})
    assert isinstance(p, Get)


def test_build_parallel():
    p = build({
        'parallel': {
            'a': {'get': 'a'},
            'b': {'get': 'b'},
        },
    })
    assert isinstance(p, Parallel)
    assert isinstance(p._processors['a'], Get)
    assert isinstance(p._processors['b'], Get)


def test_build_serial():
    p = build([
        {'get': 'a'},
        {'get_dummies': {}},
    ])
    assert isinstance(p, Serial)
    assert isinstance(p._processors[0], Get)
    assert isinstance(p._processors[1], GetDummies)
