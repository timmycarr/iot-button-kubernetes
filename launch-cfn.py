mport boto3

cfn = boto3.client('cloudformation',)

response = cfn.create_stack(
    StackName='Heptio-QS-Kubernetes-4',
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
            "ParameterValue": "your-key-here"
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
print(response)