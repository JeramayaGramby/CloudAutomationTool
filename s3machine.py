import os
from decouple import config
import boto3

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_ROOT)


# The session token must be changed every 18 hours!
ACCESS_KEY = config('ACCESS_KEY')
SECRET_ACCESS_KEY = config('SECRET_ACCESS_KEY')
SESSION_TOKEN = config('SESSION_TOKEN')
KEY_NAME = config('KEY_NAME')
KEY_PAIR_PATH = config('KEY_PAIR_PATH')
AMI_ID = config('AMI_ID')
BUCKET_NAME = config('BUCKET_NAME')



session = boto3.Session(
aws_access_key_id=ACCESS_KEY, 
aws_secret_access_key=SECRET_ACCESS_KEY, 
aws_session_token=SESSION_TOKEN
)

s3_client = boto3.client('s3')

class s3machine:
    def bucket_creator(Bucket_Name):
        try:
            s3_client.create_bucket(Bucket=BUCKET_NAME)
            print(f'Your bucket named {Bucket_Name} has successfully been created')
        except Exception as e:
            print(f'Bucket cannot be created. Try entering a new unique name or checking your environment variables')
            print(e)
    
    def bucket_remover(Bucket_Name):
        try:
            s3_client.delete_bucket(Bucket=Bucket_Name)
            print(f'Your bucket named {Bucket_Name} has successfully been deleted')
        except Exception as e:
            print(f'Bucket cannot be deleted. Try reentering the bucket name or checking your environment variables')
    
    def file_uploader(file_name,bucket,object_name):
        try:
            s3_client.upload_file(file_name,bucket,object_name)
            print(f'Your file {file_name} has been successfully uploaded to {bucket} with the name {object_name}')
        except Exception as e:
            print(f'File cannot be uploaded. Try reentering the parameters or checking your environment variables')
    
    def file_remover(bucket,object_name):
        try:
            s3_client.delete_object(Bucket=bucket,Key=object_name)
            print(f'Your file {object_name} has been successfully deleted from {bucket}')
        except Exception as e:
            print(f'File cannot be deleted. Try reentering the parameters or checking your environment variables')


if __name__ == '__main__':
    #s3machine.bucket_creator(Bucket_Name=BUCKET_NAME)
    s3machine.bucket_remover(Bucket_Name=BUCKET_NAME)
    #s3machine.file_uploader(file_name='',Bucket_Name=BUCKET_NAME,object_name='')
    #s3machine.file_remover(Bucket_Name=BUCKET_NAME,object_name='')


