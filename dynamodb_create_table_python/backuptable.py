import boto3

db = boto3.client('dynamodb')
'''
response = db.create_backup(
    TableName= 'employe',
    BackupName= 'backuptable1'
)

print(response)
'''

response = db.delete_backup(

    BackupArn= 'arn:aws:dynamodb:ap-south-1:459949273016:table/employe/backup/01677774511053-17890267'
)

print(response)