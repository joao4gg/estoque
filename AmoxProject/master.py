import base64
import json

from django.db import connections


def basic_encode(obj_list):
    encode = base64.urlsafe_b64encode(json.dumps(obj_list).encode('ascii'))
    return encode.decode('ascii')


def basic_decode(token):
    decode = token.encode('ascii')
    decode = base64.standard_b64decode(decode)
    return json.loads(decode.decode('ascii'))


def custom_query(query, database='default'):
    with connections[database].cursor() as cursor:
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
