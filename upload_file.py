import boto3
folder_path = "s3://zmx-training-bucketbatch2025/Steven/"

s3 = boto3.client('s3')
bucket_name = 'zmx-training-bucketbatch2025'
file_name = 'employee_data.parquet'

s3.upload_file(file_name, bucket_name, 'Steven/'+file_name)

print('file is uploaded')
