## AWS Automation using Python SDK boto 3:

# Command to create an S3 bucket using python boto 3

import boto3
client=boto3.client("s3")
s3=boto3.resource("s3")
print("enter bucet name")
bucket_name=input()
print("enter your region")
region=input()
def create_s3_bucket(bucket_name,region):
    
    response = s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint':region,
    },
    )

    #print(response)
    # Specify the bucket name you wish to create
    try:
         print(f"S3 bucket with bucket name '{response}' created successfully")
         return True
    except Exception as e:
        
        print(f"An error occurred while creating the S3 bucket:")
        return None
    

create_s3_bucket(bucket_name,region)

# To create an environment for the above code in EC2 connect, so following;
# Once all installments have been completed to integrate to AWS

#  compile the install in a boto3.sh bin bash

1. Create the file using vi create-bucket.py

2. paste code 

3. Then save the file using ESC:wq!

4. Then cat create-bucket.py to check the contents of the file

5. check python is running on EC2 instance "python3 create-bucket.py"

6. Then enter the buket name, region as parameters

7. This shows bucket has been created.

8. To see the contents of the S3 bucket, type aws s3 ls.
 






