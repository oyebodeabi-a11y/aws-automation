#!/bin/bash


# ami-04d29b6f966df1537 = Amazon Linux 2
aws ec2 run-instances  \
--region eu-west-2 \
--image-id "ami-04d29b6f966df1537" \
--count 1 \
--instance-type t3.micro  \
--subnet-id "subnet-087315342f5087282" \
--security-group-ids "sg-0af09b7426dbf2c40" \
--associate-public-ip-address \
--key-name "Abi1.pem" \
--user-data = "


echo \"<h1>$(curl https://api.kanye.rest/?format=text)</h1>\" >  /usr/share/nginx/html/index.html 
systemctl enable nginx
systemctl start nginx
