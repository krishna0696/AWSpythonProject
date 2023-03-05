import boto3
'''
bucket= boto3.client('s3')

response = bucket.list_buckets()

print("listing all buckets")

for bucket in response['Buckets']:
    print(bucket)  #if u=you need only name then add bucket['Name']
    
    '''
resource = boto3.resource('s3')

iterator = resource.buckets.all()

print("listing all buckets")

for bucket in iterator:
    print(bucket)   #for only bucket name use bucket.name