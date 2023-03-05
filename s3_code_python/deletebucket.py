import boto3
'''
client = boto3.client('s3')

bucket_name="oneway12345678"

client.delete_bucket(Bucket=bucket_name)

print("s3 bucket has been deleted")
'''
resource=boto3.resource('s3')

bucket_name="qwertybucket12"

s3_bucket= resource.Bucket(bucket_name)

s3_bucket.delete()
print(f'this bucket is deleted')