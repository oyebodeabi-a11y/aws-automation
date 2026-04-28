import boto3

print("please enter your action to take")
action=input()
print("please enter your region")
region=input()
print("please enter instance_ID")
instance_id=input()
def manage_ec2_instance(instance_id,region, action):
    """
    Start or stop an EC2 instance.
    :param instance_id: str, The ID of the EC2 instance
    :param action: str, 'start' to start the instance, 'stop' to stop the instance
    """
    ec2 = boto3.client('ec2', region_name=region)
    
    if action.lower() == 'start':
        response = ec2.start_instances(InstanceIds=[instance_id])
        print(f"Starting instance {instance_id}")
    elif action.lower() == 'stop':
        response = ec2.stop_instances(InstanceIds=[instance_id])
       
        print(f"Stopping instance {instance_id}")
    elif action.lower() == 'terminate':
        response = ec2.terminate_instances(InstanceIds=[instance_id])
       
        print(f"Shotting down instance {instance_id}")
    else:
        print("Invalid action. Please use 'start' or 'stop' or 'terminate'.")

manage_ec2_instance(instance_id,region,action)
