import os
from decouple import config
import boto3
import json

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_ROOT)


# The session token must be changed every 18 hours!
ACCESS_KEY = config('ACCESS_KEY')
SECRET_ACCESS_KEY = config('SECRET_ACCESS_KEY')
SESSION_TOKEN = config('SESSION_TOKEN')
KEY_NAME = config('KEY_NAME')
KEY_PAIR_PATH = config('KEY_PAIR_PATH')
AMI_ID = config('AMI_ID')

session = boto3.Session(
aws_access_key_id=ACCESS_KEY, 
aws_secret_access_key=SECRET_ACCESS_KEY, 
aws_session_token=SESSION_TOKEN
)

instance_type = 't2.micro'
region_name = 'us-east-1'
ec2_data_file = 'Boto3Project/ec2_data_file.json'

ec2_client = boto3.client('ec2', region_name=region_name)

class ec2machine:
    def ec2_creator():
        try:
            instances = ec2_client.run_instances(
                ImageId=AMI_ID,
                MinCount=1,
                MaxCount=1,
                InstanceType=instance_type,
                KeyName=KEY_NAME
            )
            return instances
        except Exception as e:
            print(f'We could not create a new EC2 instance. Please try again')
            print(e)
    
    def running_ec2_finder():
        try:
            response=ec2_client.describe_instances(
                Filters=[
                {
            'Name': 'instance-state-name',
            'Values': [
                'running',
                    ]
                },
                ],
                InstanceIds=[
                
                        ],
                DryRun=False,
            )
            
            with open("ec2_data_file.json", "w") as output_file:
                json.dump(response, output_file, default=str,sort_keys=True)
            
            print(f'Your list of running EC2s are posted inside of ec2_data_file.json')
            return response
        
        except Exception as e:
            print(f'We could not find your running EC2 instances. Please try again')
            print(e)

    def stopped_ec2_finder():
        try:
            response=ec2_client.describe_instances(
                Filters=[
                {
            'Name': 'instance-state-name',
            'Values': [
                'stopped',
                    ]
                },
                ],
                InstanceIds=[
                
                        ],
                DryRun=False,
            )
            
            with open("stopped_ec2_instances.json", "w") as output_file:
                json.dump(response, output_file, default=str,sort_keys=True)
            
            print(f'Your list of stopped EC2s are posted inside of stopped_ec2_instances.json')
            return response
        
        except Exception as e:
            print(f'We could not find your stopped EC2 instances. Please try again')
            print(e)
    
    def ec2_rebooter(instance_id):
        try:
            ec2_client.reboot_instances(InstanceIds=[instance_id])
            print(f'Your EC2 instance {instance_id} has been rebooted')
        except Exception as e:
            print(f'Your EC2 instance {instance_id} was unable to reboot. Reenter the instance id or check the environment variables')
            print(e)

    def ec2_stopper(instance_id):
        try:
            ec2_client.stop_instances(InstanceIds=[instance_id])
            print(f'Your EC2 instance {instance_id} has been stopped')
        except Exception as e:
            print(f'Your EC2 instance {instance_id} was unable to stop. Reenter the instance id or check the environment variables')
            print(e)
    
    def ec2_starter(instance_id):
        try:
            ec2_client.start_instances(InstanceIds=[instance_id])
            print(f'Your EC2 instance {instance_id} has been started successfully')
        except Exception as e:
            print(f'Your EC2 instance {instance_id} was unable to start. Reenter the instance id or check the environment variables')
            print(e) 


if __name__ == '__main__':

    # ec2machine.ec2_creator()
    #ec2machine.running_ec2_finder()
    ec2machine.stopped_ec2_finder()
    # ec2machine.ec2_rebooter(instance_id='')
    # ec2machine.ec2_stopper(instance_id='')
    # ec2machine.ec2_starter(instance_id='')