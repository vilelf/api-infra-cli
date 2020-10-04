from src.processor import Processor
from unittest import mock

@mock.patch('boto3.client')
def test_list_instances(client_mock):
    client_mock().describe_instances.return_value = {
        'Reservations': [
            {
            'Instances': []
            }
        ]
    }
    processor = Processor()
    actual = processor.list_instances()
    assert actual == {'instances': []}
