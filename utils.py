import datetime
import json


def make_response(body, status_code, headers={}):
    response = {
        'body': json.dumps(body, default=datetime_handler),
        'status_code': status_code,
        'headers': headers
    }
    return response


def datetime_handler(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError("Unknown type")
