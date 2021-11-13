import boto3
import json
import os
s3_client = boto3.client('s3')



resonse = s3_client.get_object(Bucket='django_onenine_ai',Key=os.getenv('AWS_ACCESS_KEY_ID'))

data = response['Body'].read()
print(data)