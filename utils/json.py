import json

def to_json(obj):
    if type(obj) is dict:
        return obj
    if type(obj) is not str:
        return json.loads(str(obj.__dict__))
    return json.loads(obj)


def dumps(obj):
    return json.dumps(obj)

