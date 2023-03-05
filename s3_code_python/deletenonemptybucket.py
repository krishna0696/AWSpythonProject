import boto3


BUCKET_NAME = "oneway12345678"

s3_resource = boto3.resource('s3')

s3_bucket = s3_resource.Bucket(BUCKET_NAME)

def cleanup():

    #delete the object first
    for s3_object in s3_bucket.objects.all():
        s3_object.delete()

    #delete bucket versioning
    for s3_object_ver in s3_bucket.object_versions.all():
        s3_object_ver.delete()

    print("s3 bucket cleaned")


cleanup()

s3_bucket.delete()

print("the bucket is deleted")