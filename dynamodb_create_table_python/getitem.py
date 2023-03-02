import boto3

db = boto3.resource('dynamodb')

table = db.Table('employe')

response = table.get_item(
    Key={
        'emp_id': "2"
    }
)

print(response['Item'])
