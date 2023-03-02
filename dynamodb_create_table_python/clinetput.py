import boto3

db = boto3.client('dynamodb')


response = db.put_item(
    TableName= 'employe',

    Item={
        'emp_id':{
            'S':'3'
        },
        'name':{
            'S':'mvks'
        },
        'age':{
            'S':'26'
        }
    }
)