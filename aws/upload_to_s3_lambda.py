import json
import boto3
import base64

def lambda_handler(event, context):
    bucket_name = event['bucket_name']
    file_content = base64.b64decode(event['file_content'])
    file_name = event['file_name']
    s3_client = boto3.client('s3')
    s3_client.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'File uploaded successfully'})
    }
