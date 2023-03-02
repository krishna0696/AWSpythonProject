import boto3

db = boto3.resource('dynamodb')
table = db.Table('employe')

table.put_item(
    Item={
        'emp_id':"6",
        'name':"team",
        'age': 24
    }
)
#the put item is only used for the one item to use more items use batchwriter