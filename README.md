# IOT Button - Heptio Quickstart

Currently a work in progress.

![alt text](https://github.com/timmycarr/iot-button-kubernetes/blob/master/iot-k8s-quickstart.png "AWS IOT Button Heptio Kubernetes Quickstart")

Requires:

* IAM Role to support AWS Lambda deploying the CloudFormation template.
* Lambda funtion built using python 2.7 and the launch-cfn.py code.
* Appropriate EC2 Key Pair created in the us-west-2 region. Feel free to customize.
* Environment Variables for the Lambda function created for stackName and keyPair.
* IOT button configured as the trigger. Single push will create the stack. Double push will destroy the stack.