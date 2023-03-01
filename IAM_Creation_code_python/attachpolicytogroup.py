import boto3


def attach_policy(policy_arn, groupname):
    iam = boto3.client('iam')

    response = iam.attach_group_policy(
        GroupName=groupname,
        PolicyArn=policy_arn
    )
    print(response)


attach_policy('arn:aws:iam::aws:policy/service-role/AWSQuickSightListIAM', 'admins12')
