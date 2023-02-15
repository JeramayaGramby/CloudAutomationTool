import os
from decouple import config
import boto3

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_ROOT)


# These must be changed!
ACCESS_KEY = config('ACCESS_KEY')
SECRET_ACCESS_KEY = config('SECRET_ACCESS_KEY')
SESSION_TOKEN = config('SESSION_TOKEN')

session = boto3.Session(
aws_access_key_id=ACCESS_KEY, 
aws_secret_access_key=SECRET_ACCESS_KEY, 
aws_session_token=SESSION_TOKEN
)

'''
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
ec2_resource = boto3.resource('ec2')
newbucket = s3_resource.Bucket('newbucket')

for obj in newbucket.objects.all():
    print(obj.key, obj.last_modified)

for instance in ec2_resource.instances():
    print(instance.id)
'''