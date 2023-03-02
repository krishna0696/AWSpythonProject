import boto3

db = boto3.resource('dynamodb')

table = db.Table('employe')

with table.batch_writer() as batch:   #with batch write we can add upto 25 item in a single go
    batch.put_item(
        Item={
            'emp_id':'11',
            'name':'sai',
            'age':'44'
        }
    )

    batch.put_item(
        Item={
            'emp_id': '12',
            'name': 'sai12',
            'age': '45'
        }
    )

    batch.put_item(
        Item={
            'emp_id': '13',
            'name': 'vks',
            'age': '44'
        }
    )