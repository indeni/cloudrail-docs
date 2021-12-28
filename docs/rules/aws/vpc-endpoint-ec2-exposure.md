# Ensure VPC Endpoint for EC2 is enabled in all VPCs in use

*Amazon Web Services (AWS) > Service Endpoints, Queuing*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
A best practice is to enforce the use of VPC Endpoints to avoid sending data destined to EC2 through the internet. Cloudrail will identify misconfigurations by checking if VPC Endpoint Interfaces are in use or not, by reviewing that an endpoint exists in the VPC. VPC Interface Endpoints might not be available in all regions, so the rule checks that if the service is running it's configured in all possible VPCs. This rule has potential false positives given that not all VPCs require communication with EC2.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Service Endpoints, Queuing
- **Rule ID**: vpc_endpoint_ec2_exposure

---

## Remediation
Information on how to fix "Ensure VPC Endpoint for EC2 is enabled in all VPCs in use" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
Create a resource aws_vpc_endpoint for EC2 interface, and associate it to the VPC.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
Create a resource AWS::EC2::VPCEndpoint for EC2 interface, and associate it to the VPC.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Create a VPC Endpoint for EC2, follow the guide at <https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint>.




---

## How It Works
For each region, Cloudrail will verify if at least one EC2 instance exists, then will also verify that the service VPC Endpoint for EC2 is available in the region, if so it will check that it's configured in all possible VPCs and will flag any non-compliant VPC.