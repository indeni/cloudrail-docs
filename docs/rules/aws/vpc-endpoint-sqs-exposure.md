# Ensure VPC Endpoint for SQS is enabled in all VPCs in use

*Amazon Web Services (AWS) > Service Endpoints, Queuing*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
A best practice is to enforce the use of VPC Endpoints to avoid sending data destined to SQS through the internet. Cloudrail will identify misconfigurations by checking if VPC Endpoint Interfaces are in use or not, by reviewing that an endpoint exists in the VPC. VPC Interface Endpoints might not be available in all regions, so the rule checks that if the service is running it's configured in all possible VPCs. This rule has potential false positives given that not all VPCs require communication with SQS.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Service Endpoints, Queuing
- **Rule ID**: vpc_endpoint_sqs_exposure

---

## Remediation
Information on how to fix "Ensure VPC Endpoint for SQS is enabled in all VPCs in use" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
Create a resource aws_vpc_endpoint for SQS interface, and associate it to the VPC.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
Create a resource AWS::EC2::VPCEndpoint for SQS interface, and associate it to the VPC.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Create a VPC Endpoint for SQS, follow the guide at <https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint>.




---

## How It Works
For each region, Cloudrail will verify if at least one SQS queue exists, then will also verify that the service VPC Endpoint for SQS is available in the region, if so it will check that it's configured in all possible VPCs and will flag any non-compliant VPC.