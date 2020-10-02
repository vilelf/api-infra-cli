import boto3

class Processor():
    def list_instances(self):
        ec2 = boto3.client('ec2', region_name='us-east-1')
        instances = ec2.describe_instances()['Reservations'][0]['Instances']
        return {'instances': instances}
