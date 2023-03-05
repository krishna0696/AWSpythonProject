import boto3

bucket = boto3.resource('s3')

response = bucket.create_bucket (
    Bucket ='oneway12345678',
    ACL='private',
    CreateBucketConfiguration= {
        'LocationConstraint':'ap-south-1'
        }
     )


print(response)
