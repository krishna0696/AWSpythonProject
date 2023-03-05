import boto3

BUCKET_NAME = "oneway12345678"

s3_resource = boto3.resource('s3')

s3_object = s3_resource.Object(BUCKET_NAME, 'file.pdf')

s3_object.download_file('downloaded.pdf')

print("file has been dowloaded")