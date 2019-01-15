import json

def user_defined_function(value):
    data = int(value) % 2
    ret = None
    if data == 0:
        wrapped = {'number': data}
        ret = json.dumps(wrapped)
    return ret
