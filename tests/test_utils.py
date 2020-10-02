import json

from utils import make_response

def test_make_response():
    body = {'asdf': 'teste'}
    status_code = 200
    headers = {'new_header': 'auth'}
    actual = make_response(body, status_code, headers)
    assert actual == {
        'body': json.dumps(body), 
        'status_code': status_code, 
        'headers': headers
    }