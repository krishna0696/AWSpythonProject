import boto3

client = boto3.client('s3')

response = client.create_bucket(
    Bucket="qwertybucket12",
    ACL= "private",

    CreateBucketConfiguration= {
        'LocationConstraint':'ap-south-1'
    }
)

print(response)