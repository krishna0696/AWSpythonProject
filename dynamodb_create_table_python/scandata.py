import boto3
from pprint import pprint
db = boto3.resource('dynamodb')

table = db.Table('employe')

response = table.scan()

data= response['Items']
print(data)