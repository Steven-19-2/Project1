import boto3
#folder_path = "s3://zmx-training-bucketbatch2025/Steven/"
s3 = boto3.client('s3')
class FileUpload:
    def __init__(self):
        pass
    
    def upload_file(self, file_name, bucket):
        s3.upload_file(file_name, bucket, 'Steven/'+file_name)
        print('File is uploaded')

if __name__ == "__main__":
    uploader = FileUpload()
    BUCKET_NAME = 'zmx-training-bucketbatch2025'
    FILE = 'employee_data.parquet'
    uploader.upload_file(FILE, BUCKET_NAME)