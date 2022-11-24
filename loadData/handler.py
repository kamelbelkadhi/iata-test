import json, io, boto3, requests

import os


s3_bucket_name=os.environ['BUCKET']
url = 'https://eforexcel.com/wp/wp-content/uploads/2020/09/2m-Sales-Records.zip'
def create_aws_resource():
    s3 = boto3.client('s3')
    return s3

def save_to_s3(url, doc_name,bucket, s3_path):
    s3 = create_aws_resource()
    response = requests.get(url, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
    s3.upload_fileobj(io.BytesIO(response.content), bucket, f'{s3_path}/{doc_name}')
    
def lambda_handler(event, context):
    # TODO implement
    save_to_s3(url, '2m-Sales-Records.zip', s3_bucket_name, 'original_data')
    return {
        'statusCode': 200,
        'body': json.dumps('Data Loaded into S3')
    }
