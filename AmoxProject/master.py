import base64
import json


def basic_encode(obj_list):
    encode = base64.urlsafe_b64encode(json.dumps(obj_list).encode('ascii'))
    return encode.decode('ascii')


def basic_decode(token):
    decode = token.encode('ascii')
    decode = base64.standard_b64decode(decode)
    return json.loads(decode.decode('ascii'))
