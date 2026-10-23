import boto3


#if you want to just reead the resource fot he followinf you will use the resource
# s3 = boto3.resource('s3')
#for more flexible work you will use client 
s3 = boto3.client('s3')

#to see the list of bueckets in s3
# for bucket in s3.buckets.all():
#     print(bucket.name)

#to upload the files in the s3 bucket using boto3
#we will use the file name , bucket name and object name == api.py her in this example

file_name = r"C:\Users\Ashwani\OneDrive\Desktop\DEVOPS\python-for-devops\MERIFILES\api.py"
object_name = "api.py"
bucket = "devops-ai-powered6"

response = s3.upload_file(file_name,bucket,object_name)
