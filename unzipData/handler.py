import gzip, io, boto3, zipfile, json



# bucket = 'kamelbuckettest'
# input_file = 'original_data/2m-Sales-Records.zip'
# output_file = 'extarcted_file/'+input_file

        
def load_unzip_file(bucket,input_file,output_file):
    s3 = boto3.resource('s3')
    zip_obj = s3.Object(bucket_name=bucket, key=input_file)
    buffer = io.BytesIO(zip_obj.get()["Body"].read())
    z = zipfile.ZipFile(buffer)
    for filename in z.namelist():
        s3.meta.client.upload_fileobj(
            z.open(filename),
            Bucket=bucket,
            Key=output_file)

def lambda_handler(event, context):
    bucket= event['Records'][0]['s3']['bucket']['name']
    input_file= event['Records'][0]['s3']['object']['key']

    output_file = 'extarcted_file/'+input_file
    output_file = output_file.replace(".zip", ".csv")
    output_file = output_file.replace("original_data/", "")
    load_unzip_file(bucket,input_file,output_file)
    return {
        'statusCode': 200,
        'body': json.dumps('Unzipped File at: '+output_file)
    }