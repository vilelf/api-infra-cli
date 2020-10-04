import json

from utils import make_response

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
