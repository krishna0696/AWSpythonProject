import boto3

def detach_group(user_group, arn):
    iam = boto3.client('iam')

    response = iam.detach_group_policy(
        GroupName=user_group,
        PolicyArn=arn
    )

    print(response)


detach_group('admins12', 'arn:aws:iam::aws:policy/service-role/AWSQuickSightListIAM')