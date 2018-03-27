import boto3
import os

client = boto3.client('cloudformation', region_name='us-west-2')


def lambda_handler(event, context):
    if 'clickType' in event:
        if event['clickType'] == 'SINGLE':
            print("Single press - Deploy the CloudFormation"),
            build_stack()
        if event['clickType'] == 'DOUBLE':
            print("Double press - Delete the CloudFormation"),
            delete_stack()
        else:
            print("Something other than a single or double click")
    else:
        print("Something other than a click called the Lambda")
    return 'end of function'   

def build_stack():
    response = client.create_stack(
        StackName=os.environ['stackName'],
        TemplateURL='https://s3.amazonaws.com/quickstart-reference/heptio/latest/templates/kubernetes-cluster-with-new-vpc.template',
        Parameters=[
            {
                "ParameterKey": "AvailabilityZone",
                "ParameterValue": "us-west-2b"
            },
            {
                "ParameterKey": "AdminIngressLocation",
                "ParameterValue": "0.0.0.0/0"
            },
            {
                "ParameterKey": "KeyName",
                "ParameterValue": os.environ['keyPair']
            },
            {
                "ParameterKey": "NetworkingProvider",
                "ParameterValue": "calico"
            },   
            {
                "ParameterKey": "K8sNodeCapacity",
                "ParameterValue": "2"
            },
            {
                "ParameterKey": "InstanceType",
                "ParameterValue": "m4.large"
            },
            {
                "ParameterKey": "DiskSizeGb",
                "ParameterValue": "40"
            },
            {
                "ParameterKey": "BastionInstanceType",
                "ParameterValue": "t2.micro"
            },
            {
                "ParameterKey": "QSS3BucketName",
                "ParameterValue": "quickstart-reference"
            },
            {
                "ParameterKey": "QSS3KeyPrefix",
                "ParameterValue": "heptio/latest"
            },
        ],
        Capabilities=[
            'CAPABILITY_IAM',
        ],
        OnFailure='ROLLBACK',
        EnableTerminationProtection=False
    )
    return(response)

def delete_stack():
    response = client.delete_stack(
        StackName=os.environ['stackName'],
    )
    return(response)
