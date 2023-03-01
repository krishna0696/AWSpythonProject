import boto3


def remove_user(group_name, username):
    iam = boto3.client('iam')

    response = iam.remove_user_from_group(
        UserName=username,
        GroupName=group_name
    )

    print(response)


remove_user ('admins12', 'seconduser')