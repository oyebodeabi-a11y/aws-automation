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

aws ec2 create-vpc --region eu-west-2 --cidr-block "10.0.0.0/16" 

# Command to create a subnet in created VPC  with a  name for the subnet

aws ec2 create-subnet \
  --region eu-west-2 \
  --cidr-block 10.0.1.0/24 \
  --availability-zone eu-west-2a \
  --vpc-id vpc-07ba92b75c7071a71 \
  --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=pub-subnet1}]'

# Command to create route table

aws ec2 create-route-table --region eu-west-2  --vpc-id "vpc-07ba92b75c7071a71"

# Command to create internet gateway

aws ec2 create-internet-gateway --region eu-west-2 

# Command this is the internet  gateway "igw-0abc430fe9187f886"

# Command for connect the internet gateway to the vpc

aws ec2 attach-internet-gateway --region eu-west-2 --internet-gateway-id "igw-0abc430fe9187f886" --vpc-id "vpc-07ba92b75c7071a71"

# Command to link  the route table to the subnet

aws ec2 associate-route-table --region eu-west-2 --route-table-id "rtb-0eea510250acfc954" --subnet-id "subnet-087315342f5087282"

aws ec2 associate-route-table --region us-east-1 --route-table-id "..." --subnet-id "..."

# Command to create security group 

aws ec2 create-security-group --region eu-west-2 --description "Allow http access over the internet" --group-name "public-sg" --vpc-id "vpc-07ba92b75c7071a71"

# Command to create security group ingress port 80 and port 22

aws ec2 authorize-security-group-ingress --region eu-west-2 --group-id "sg-0e30ea178419b9d25" --protocol "tcp" --port "80" --cidr "0.0.0.0/0"
aws ec2 authorize-security-group-ingress --region eu-west-2 --group-id "sg-0e30ea178419b9d25" --protocol "tcp" --port "22" --cidr "0.0.0.0/0"

# Command to create EC2 instance with existing key pair

aws ec2 run-instances  --region eu-west-2 --image-id "ami-0685f8dd865c8e389" --count 1 --instance-type t3.micro  --subnet-id "subnet-087315342f5087282" --security-group-ids "sg-0af09b7426dbf2c40" --associate-public-ip-address --key-name "abi"

# Command  to  terminate EC2  instance

aws ec2 terminate-instances --instance-ids i-08e870ec9e18b54fd

