# Ensure VPC Endpoint for SQS is enabled in all Availability Zones in use a VPC

*Amazon Web Services (AWS) > Service Endpoints, Queuing*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
A best practice is to enforce the use of VPC Endpoints to avoid sending data destined to SQS through the internet. Cloudrail will identify misconfigurations by checking if VPC Endpoint Interfaces are in use or not, by reviewing that an endpoint exists in the VPC. VPC Interface Endpoints are not available in all availability zones, also they can be configured in just one subnet per availability zone, so the rule checks that if the service is running it's configured in at least two availability zones in use and leaves the traffic architecture decision to the customer. Additionally, make sure that if the application is using the custom hostnames for the service, and if it's using default hostnames (I.e. sqs.us-east-2.amazonaws.com) that the application is using Amazon DNS and not an internal DNS.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Service Endpoints, Queuing
- **Rule ID**: vpc_endpoint_sqs_subnet_exposure

---

## Remediation
Information on how to fix "Ensure VPC Endpoint for SQS is enabled in all Availability Zones in use a VPC" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
Locate resource aws_vpc_endpoint for SQS interface, and make sure that argument subnet_ids contains at least one subnet in each Availability Zone in use. Interface endpoints do have their costs, so if that’s an issue, consider using at least two interface endpoints in different availability zones, and not just one.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
Locate resource AWS::EC2::VPCEndpoint for SQS interface, and make sure that argument SubnetIds contains at least one subnet in each Availability Zone in use. Interface endpoints do have their costs, so if that’s an issue, consider using at least two interface endpoints in different availability zones, and not just one.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
For each VPC that is currently using VPC endpoints for SQS, make sure it’s enabled in one subnet for each Availability Zone in use. Follow the guide at <https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint>. Interface endpoints do have their costs, so if that’s an issue, consider using at least two interface endpoints in different availability zones, and not just one.




---

## How It Works
For each region, Cloudrail will verify if at least one SQS queue exists, then will also verify that the service VPC Endpoint for SQS is available in the region and in which availability zones. It will also check all subnets in use, and check all subnets that may have an endpoint configured. It will then check to see that at least two of the availability zones in use have an interface endpoint in them.