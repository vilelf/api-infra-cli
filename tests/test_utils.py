import json
from datetime import datetime
from typing import Type

import pytest
from utils import datetime_handler, make_response


def test_make_response():
    body = {'asdf': 'teste'}
    status_code = 200
    headers = {'Content-Type': 'json', 'new_header': 'auth'}
    actual = make_response(body, status_code, headers)
    assert actual == {
        'body': json.dumps(body), 
        'statusCode': status_code, 
        'headers': headers
    }


def test_datetime_handler_on_datetime_passed():
    now = datetime(year=2020, month=10, day=4, hour=22, minute=9)
    actual = datetime_handler(now)
    expected = '2020-10-04T22:09:00'
    assert actual == expected


def test_datetime_handler_on_not_datetime_passed():
    with pytest.raises(TypeError):
        datetime_handler('asdf')
