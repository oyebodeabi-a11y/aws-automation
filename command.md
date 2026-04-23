## Commands to automake AWS S3 bucket tasks:

# Command to copy files to s3 bucket

aws s3 cp secret s3://awstraining-abby1/ --recursive

# Command to move files into s3 bucket

aws s3 mv secret s3://awstraining-abby1/ --recursive

# Command to copy files from s3 bucket in aws to a folder on the desktop

aws s3 cp s3://awstraining-abby1 freshsecret/ --recursive

# Command to move files from s3 bucket in aws to a folder on the desktop

aws s3 mv s3://awstraining-abby1 topaccess/ --recursive

# Command to remove the contents of the s3 bucket in aws

aws s3 rm s3://awstraining-abby1/ --recursive

# Command to delete an aws s3 bucket

 aws s3api delete-bucket --bucket awstraining-abby1 --region eu-west-2

 ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 ## Commands to automate tasks for IAM user

 # command to create an IAM user

aws iam create-user --user-name Bob

# command to list iam users

aws iam list-users

# command to delete an iam  user

aws iam delete-user --user-name Bob

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Commands for key pairs

# Command to create key pairs
aws ec2 create-key-pair --key-name myKeyPair

# Command to list key pairs

aws ec2 describe-key-pairs

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Comands for VPC

# Command to create VPC
AWS_VPC_INFO=$(aws ec2 create-vpc \
--cidr-block 10.0.0.0/16 \
--query 'Vpc.{VpcId:VpcId}' \
--output text)

# Command to create a subnet in created VPC

AWS_SUBNET_PUBLIC=$(aws ec2 create-subnet \
--vpc-id $AWS_VPC_INFO --cidr-block 10.0.1.0/24 \
--availability-zone us-east-1a --query 'Subnet.{SubnetId:SubnetId}' \
--output text)


