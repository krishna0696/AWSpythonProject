import boto3

iam = boto3.client('iam')

response = iam.detach_user_policy(
    UserName='mvks',
    PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess'
)

print(response)