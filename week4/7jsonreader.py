a= {u'results': [{u'alternatives': [{u'confidence': 1, u'transcript':
u'Halo', u'words': [{u'endTime': u'2s', u'word': u'Halo', u'startTime':
u'0.400s'}]}]}, {u'alternatives': [{u'confidence': 0.98715955,
u'transcript': u' hola', u'words': [{u'endTime': u'8s', u'word':
u'hola', u'startTime': u'4.100s'}]}]}]}

def find_key(obj, key):
    if isinstance(obj, dict):
        yield from iter_dict(obj, key, [])
    elif isinstance(obj, list):
        yield from iter_list(obj, key, [])

def iter_dict(d, key, indices):
    for k, v in d.items():
        if k == key:
            yield indices + [k], v
        if isinstance(v, dict):
            yield from iter_dict(v, key, indices + [k])
        elif isinstance(v, list):
            yield from iter_list(v, key, indices + [k])

def iter_list(seq, key, indices):
    for k, v in enumerate(seq):
        if isinstance(v, dict):
            yield from iter_dict(v, key, indices + [k])
        elif isinstance(v, list):
            yield from iter_list(v, key, indices + [k])

for t in find_key(a, 'startTime'):
    print(t)