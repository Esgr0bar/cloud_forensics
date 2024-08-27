import boto3

class CloudHandler:
    def __init__(self, cloud_provider='aws'):
        if cloud_provider == 'aws':
            self.client = boto3.client('ec2')
        # to do : Additional setup for Azure, GCP

    def create_snapshot(self, instance_id):
        response = self.client.create_snapshot(
            Description='Forensic Snapshot',
            InstanceId=instance_id
        )
        return response['SnapshotId']

    def create_vm_from_snapshot(self, snapshot_id):
        response = self.client.run_instances(
            ImageId=snapshot_id,
            MinCount=1,
            MaxCount=1,
            InstanceType='t2.micro'
        )
        return response['Instances'][0]['InstanceId']
