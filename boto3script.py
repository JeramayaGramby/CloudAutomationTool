import os
from decouple import config
import boto3
import json

ACCESS_KEY=str(input(f'Enter your Access Key:'))
SECRET_ACCESS_KEY=str(input(f'Enter your Secret Access Key:'))
SESSION_TOKEN=str(input(f'Enter your session token:'))
region_name=str(input('What region would you like to work from? (ex: us-east-1):'))


session = boto3.Session(
aws_access_key_id=ACCESS_KEY, 
aws_secret_access_key=SECRET_ACCESS_KEY, 
aws_session_token=SESSION_TOKEN
)



s3_client = boto3.client('s3')
ec2_client = boto3.client('ec2', region_name=region_name)

class ec2machine:
    def ec2_creator():
        try:
            instance_type=str(input('What instance type would you like to create (ex: t2.micro):'))
            AMI_ID=str(input('What AMI ID would you like to use?:'))
            KEY_NAME=str(input('What is the name of the Key Pair you would like to use? (ex:KeyPair1):'))
            instances = ec2_client.run_instances(
                ImageId=AMI_ID,
                MinCount=1,
                MaxCount=1,
                InstanceType=instance_type,
                KeyName=KEY_NAME
            )
            print(f'You have successfully deployed an EC2 instance! To see a description of the instance check for running instances.')
            return instances
        except Exception as e:
            print(f'We could not create a new EC2 instance. Please try again')
            print(e)
    
    def running_ec2_finder():
        try:
            ec2_data_file=str(input('Where would you like to save the data file? (ex:ProjectFolder/ec2_data_file.json):'))
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
            
            with open(ec2_data_file, "w") as output_file:
                json.dump(response, output_file, default=str,sort_keys=True)
            
            print(f'Your list of running EC2s are posted inside of ec2_data_file.json')
            return response
        
        except Exception as e:
            print(f'We could not find your running EC2 instances. Please try again')
            print(e)

    def stopped_ec2_finder():
        try:
            ec2_data_file=str(input('Where would you like to save the data file? (ex:ProjectFolder/ec2_data_file.json):'))
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
            
            with open(ec2_data_file, "w") as output_file:
                json.dump(response, output_file, default=str,sort_keys=True)
            
            print(f'Your list of stopped EC2s are posted inside of stopped_ec2_instances.json')
            return response
        
        except Exception as e:
            print(f'We could not find your stopped EC2 instances. Please try again')
            print(e)
    
    def ec2_rebooter():
        try:
            instance_id=str(input('What is the instance id for the instance you would like to reboot?'))
            ec2_client.reboot_instances(InstanceIds=[instance_id])
            print(f'Your EC2 instance {instance_id} has been rebooted')
            return instance_id
        except Exception as e:
            print(f'Your EC2 instance {instance_id} was unable to reboot.')
            print(e)

    def ec2_stopper():
        try:
            instance_id=str(input('What is the instance id for the instance you would like to stop?'))
            ec2_client.stop_instances(InstanceIds=[instance_id])
            print(f'Your EC2 instance {instance_id} has been stopped')
            return instance_id
        except Exception as e:
            print(f'Your EC2 instance {instance_id} was unable to stop.')
            print(e)
    
    def ec2_starter():
        try:
            instance_id=str(input('What is the instance id for the instance you would like to start?'))
            ec2_client.start_instances(InstanceIds=[instance_id])
            print(f'Your EC2 instance {instance_id} has been started successfully')
            return instance_id
        except Exception as e:
            print(f'Your EC2 instance {instance_id} was unable to start.')
            print(e) 

    


class s3machine:
    def bucket_creator():
        try:
            Bucket_Name=str(input(f'Enter the bucket name of the bucket you would like to create:'))
            s3_client.create_bucket(Bucket=Bucket_Name)
            print(f'Your bucket named {Bucket_Name} has successfully been created')
            return Bucket_Name
        except Exception as e:
            print(f'Bucket cannot be created.')
            print(e)
    
    def bucket_remover():
        try:
            Bucket_Name=str(input(f'Enter the bucket name of the bucket you would like to destroy:'))
            s3_client.delete_bucket(Bucket=Bucket_Name)
            print(f'Your bucket named {Bucket_Name} has successfully been deleted')
            return Bucket_Name
        except Exception as e:
            print(f'Bucket cannot be deleted.')
            print(e)
    
    def file_uploader():
        try:
            file_name=str(input(f'Enter the name of the file you would like to upload (ex:example.txt):'))
            bucket=str(input(f'Enter the bucket name of the bucket you would like to create:'))
            object_name=str(input(f'Enter the object name for the file you would like to upload:'))
            s3_client.upload_file(file_name,bucket,object_name)
            print(f'Your file {file_name} has been successfully uploaded to {bucket} with the name {object_name}')
            return file_name,object_name,bucket
        except Exception as e:
            print(f'File cannot be uploaded.')
            print(e)
    
    def file_remover():
        try:
            bucket=str(input(f'Enter the name of the bucket that holds your file'))
            object_name=str(input(f'Enter the object name for the file you would like to delete'))
            s3_client.delete_object(Bucket=bucket,Key=object_name)
            print(f'Your file {object_name} has been successfully deleted from {bucket}')
            return bucket,object_name
        except Exception as e:
            print(f'File cannot be deleted.')
            print(e)


try:
    question_1=input(f'Enter ec2 to use the EC2 machine or enter s3 to use the S3 Machine:')
    if str(question_1) == 'ec2':
        question_2=input(f'Enter 1 to create a new instance, Enter 2 to find all running EC2 instances, Enter 3 to find all stopped EC2 instances, Enter 4 to reboot an instance, Enter 5 to stop an instance, Enter 6 to start an instance:')
        if str(question_2) == '1':
            ec2machine.ec2_creator()
        if str(question_2) == '2':
            ec2machine.running_ec2_finder()
        if str(question_2) == '3':
            ec2machine.stopped_ec2_finder()
        if str(question_2) == '4':
            ec2machine.ec2_rebooter()
        if str(question_2) == '5':
            ec2machine.ec2_stopper()
        if str(question_2) == '6':
            ec2machine.ec2_starter()

    if str(question_1) == 's3':
        question_3=input(f'Enter 1 to create a new bucket, Enter 2 to delete a bucket, Enter 3 to upload a file, Enter 4 to delete a file:')
        if str(question_3) == '1':
            s3machine.bucket_creator()
        if str(question_3) == '2':
            s3machine.bucket_remover()
        if str(question_3) == '3':
            s3machine.file_uploader()
        if str(question_3) == '4':
            s3machine.file_remover()

except Exception as e:
    print(f'One or more of your inputs was invalid. Please rerun the script.')
    print(e)