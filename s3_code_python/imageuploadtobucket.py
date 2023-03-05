import boto3

client = boto3.client('s3')

with open('awas.png','rb')as f:
    data = f.read()


response = client.put_object(
    ACL="public-read", #or private
    Bucket="oneway12345678",
    Body=data,
    Key='awas.png'
)

print(response)