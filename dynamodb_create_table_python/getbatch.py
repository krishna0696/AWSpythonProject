import boto3
from pprint import pprint
db = boto3.resource('dynamodb')

response = db.batch_get_item(
    RequestItems={
        'employe':{
            'Keys':[
                {
                    'emp_id':'1',
                },
                {
                    'emp_id':'11',
                },
                {
                    'emp_id':'13'
                }
            ]
        }
    }
)

print(response['Responses'])