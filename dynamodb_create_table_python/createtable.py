import boto3

def create_movie_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.create_table(
        TableName='movies',
        KeySchemes=[
            {
                'AttributeName':'year',
                'KeyType':'HASH'
            },
            {
                'AttributeName':'title',
                'KeyType':'RANGE'
            }
        ]

        AttributeDefinitions=[
            {
                'AttributeName': 'year',
                'AttributeType': 'N'
            }
        ]
    )