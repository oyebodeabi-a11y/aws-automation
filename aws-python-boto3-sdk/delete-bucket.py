# To list the buckets created in S3: aws s3 ls.

# To delete the S3 bucket: science1505abio

1. import boto3

s3 = boto3.resource("s3")
client = boto3.client("s3")

def delete_s3_bucket(bucket_name):
    try:
        bucket = s3.Bucket(bucket_name)

        # Delete everything inside
        bucket.objects.all().delete()
        bucket.object_versions.delete()  # safe even if versioning is off

        # Delete bucket
        client.delete_bucket(Bucket=bucket_name)

        print(f"S3 bucket '{bucket_name}' deleted successfully")

    except Exception as e:
        print(f"Error: {e}")


bucket_name = input("Enter bucket name to delete: ")
delete_s3_bucket(bucket_name)

steps to follow:

1. Create the file using vi delete-bucket.py

2. paste code 

3. Then save the file using ESC:wq!

4. Then cat delete-bucket.py to  check the contents of the file

5. check python is running on EC2 instance "python3 delete-bucket.py"

6. Then enter the bucket name to  delete: science1505abio

7. This shows bucket has been deleted.

