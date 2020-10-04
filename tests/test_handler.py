from unittest import mock

from src.handler import list_instances


@mock.patch('boto3.client')
def test_list_instances(mock_client):
    mock_client().describe_instances.return_value = {
        'Reservations': [{'Instances': []}]
    }
    actual = list_instances({}, {})
    expected = {
        'body': '{"instances": []}',
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'}
    }
    assert actual == expected
