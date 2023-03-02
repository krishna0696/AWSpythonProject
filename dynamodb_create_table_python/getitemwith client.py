import boto3

db = boto3.client('dynamodb')

response = db.get_item(
    TableName='employe',
    Key={
        'emp_id':{
            'S':'11'
        }
    }
)

print(response)