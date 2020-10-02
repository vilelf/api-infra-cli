import datetime
import json


def make_response(body, status_code, headers={}):
    default_headers = {'Content-Type': 'application/json'}
    default_headers.update(headers)
    response = {
        'body': json.dumps(body, default=datetime_handler),
        'statusCode': status_code,
        'headers': default_headers
    }
    return response


def datetime_handler(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError("Unknown type")
