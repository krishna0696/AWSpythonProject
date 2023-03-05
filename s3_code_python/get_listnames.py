import boto3


BUCKET_NAME = "oneway12345678"

s3_resource = boto3.resource('s3')

s3_bucket = s3_resource.Bucket(BUCKET_NAME)

print("listing bucket files or objects")

for obj in s3_bucket.objects.all():
    print(obj.key)