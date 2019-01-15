import json

def user_defined_function(value):
    data = int(value)
    ret = None
    if data % 2 != 0:
        wrapped = {'number': data}
        ret = json.dumps(wrapped)
    return ret
