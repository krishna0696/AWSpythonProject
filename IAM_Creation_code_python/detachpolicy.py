import boto3

iam = boto3.client('iam')

response = iam.detach_user_policy(
    UserName='seconduser',
    PolicyArn='arn:aws:iam::459949273016:policy/pyFullAccess'
)

print(response)