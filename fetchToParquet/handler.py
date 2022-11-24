import pandas as pd
import s3fs
import awswrangler as wr
import json
        
def lambda_handler(event, context):
    # TODO implement
    bucket= event['Records'][0]['s3']['bucket']['name']
    key= event['Records'][0]['s3']['object']['key']
    data = pd.read_csv('s3://'+bucket+'/'+key)
    data.columns = [column.replace(' ', '_') for column in data.columns]
    wr.s3.to_parquet(
        df=data,
        path='s3://'+bucket+'/output_data/',
        dataset=True,
        partition_cols=['Country'])
    return {
        'statusCode': 200,
        'body': json.dumps('Data Loaded into S3')
    }

