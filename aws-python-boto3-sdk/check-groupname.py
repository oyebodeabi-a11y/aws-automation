# The AWS SDK for Python (Boto3) provides a Python API for AWS infrastructure services. Using the SDK for Python, you can build applications on top of Amazon S3, Amazon EC2, Amazon DynamoDB, and more.

import boto3
iam=boto3.resource('iam')
print("enter the group name to search")
groupname = input()
def list_iam_users_group():
    
    print('connecting to Iam')
   # iam=boto3.resource('iam')
    group=iam.Group(groupname).users.all()
   
    #create list of users
    print('list of users')
    names=[i.name for i in group]
   
    print(names)
    #return names

list_iam_users_group()