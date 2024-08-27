import boto3
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from google.cloud import compute_v1
from google.auth import default

class CloudHandler:
    def __init__(self, cloud_provider='aws'):
        self.cloud_provider = cloud_provider
        if cloud_provider == 'aws':
            self.client = boto3.client('ec2', region_name='us-east-1')
        elif cloud_provider == 'azure':
            self.credential = DefaultAzureCredential()
            self.subscription_id = 'your-azure-subscription-id'
            self.client = ComputeManagementClient(self.credential, self.subscription_id)
        elif cloud_provider == 'gcp':
            self.client = compute_v1.InstancesClient()
            self.project_id, self.credentials = default()
            self.zone = 'your-gcp-zone'

    def create_snapshot(self, instance_id):
        if self.cloud_provider == 'aws':
            response = self.client.create_snapshot(
                Description='Forensic Snapshot',
                InstanceId=instance_id
            )
            return response['SnapshotId']
        elif self.cloud_provider == 'azure':
            # Assuming instance_id is the name of the VM in Azure
            snapshot_name = f"{instance_id}-snapshot"
            async_snapshot_creation = self.client.snapshots.begin_create_or_update(
                'your-resource-group-name',
                snapshot_name,
                {
                    "location": 'your-region',
                    "creation_data": {
                        "create_option": "Copy",
                        "source_uri": f"/subscriptions/{self.subscription_id}/resourceGroups/your-resource-group-name/providers/Microsoft.Compute/disks/{instance_id}"
                    }
                }
            )
            snapshot = async_snapshot_creation.result()
            return snapshot.name
        elif self.cloud_provider == 'gcp':
            snapshot_name = f"{instance_id}-snapshot"
            operation = self.client.create_snapshot(
                project=self.project_id,
                zone=self.zone,
                instance=instance_id,
                snapshot_resource={"name": snapshot_name}
            )
            operation.result()  # Waits for the operation to complete
            return snapshot_name

    def create_vm_from_snapshot(self, snapshot_id):
        if self.cloud_provider == 'aws':
            response = self.client.run_instances(
                ImageId=snapshot_id,
                MinCount=1,
                MaxCount=1,
                InstanceType='t2.micro'
            )
            return response['Instances'][0]['InstanceId']
        elif self.cloud_provider == 'azure':
            async_vm_creation = self.client.virtual_machines.begin_create_or_update(
                'your-resource-group-name',
                'new-vm-name',
                {
                    "location": 'your-region',
                    "storage_profile": {
                        "os_disk": {
                            "create_option": "FromImage",
                            "image": {
                                "id": f"/subscriptions/{self.subscription_id}/resourceGroups/your-resource-group-name/providers/Microsoft.Compute/snapshots/{snapshot_id}"
                            }
                        }
                    },
                    "hardware_profile": {
                        "vm_size": "Standard_DS1_v2"
                    },
                    "os_profile": {
                        "computer_name": 'new-vm-name',
                        "admin_username": 'your-admin-username',
                        "admin_password": 'your-admin-password'
                    },
                    "network_profile": {
                        "network_interfaces": [
                            {
                                "id": "your-network-interface-id",
                                "primary": True
                            }
                        ]
                    }
                }
            )
            vm = async_vm_creation.result()
            return vm.name
        elif self.cloud_provider == 'gcp':
            new_instance_name = f"new-instance-from-{snapshot_id}"
            instance = compute_v1.Instance(
                name=new_instance_name,
                disks=[
                    compute_v1.AttachedDisk(
                        auto_delete=True,
                        boot=True,
                        initialize_params=compute_v1.AttachedDiskInitializeParams(
                            source_snapshot=snapshot_id
                        )
                    )
                ],
                machine_type=f"zones/{self.zone}/machineTypes/n1-standard-1",
                network_interfaces=[
                    compute_v1.NetworkInterface(
                        name="global/networks/default"
                    )
                ]
            )
            operation = self.client.insert(
                project=self.project_id,
                zone=self.zone,
                instance_resource=instance
            )
            operation.result()  # Waits for the operation to complete
            return new_instance_name
