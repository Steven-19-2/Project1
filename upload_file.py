import boto3
#folder_path = "s3://zmx-training-bucketbatch2025/Steven/"

s3 = boto3.client('s3')
BUCKET_NAME = 'zmx-training-bucketbatch2025'
FILE_NAME = 'employee_data.parquet'

s3.upload_file(FILE_NAME, BUCKET_NAME, 'Steven/'+FILE_NAME)

print('file is uploaded')
