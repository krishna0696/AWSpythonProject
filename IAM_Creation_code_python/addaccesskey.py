import boto3
'''
def create_access(username):
    iam = boto3.client('iam')

    response = iam.create_access_key(
        UserName=username
    )

    print(response)


create_access('seconduser')
'''

def update_access():
    iam = boto3.client('iam')
    response = iam.update_access_key(
        AccessKeyId='AKIAWWFY4564KANHVL4B',
        Status='Inactive',
        UserName='seconduser'
    )
    print(response)

update_access()