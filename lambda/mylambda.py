import json
import boto3
import os



def handler(event, context):
    filename = 'my_file.txt'
    
    s3 = boto3.resource('s3')
    file = s3.Object(os.environ['BUCKET_NAME'], 'my_file.txt')
    file_content = file.get()['Body'].read().decode('utf-8')
    #print('request: {}'.format(json.dumps(event)))
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': file_content
    }
