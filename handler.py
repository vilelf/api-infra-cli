from processor import Processor
from utils import make_response

def list_instances(event, context):
    processor = Processor()
    instances = processor.list_instances()
    return make_response(instances, 200)
