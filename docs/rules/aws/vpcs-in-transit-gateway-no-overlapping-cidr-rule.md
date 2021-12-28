# VPC's in Transit Gateway should not have common CIDR's

*Amazon Web Services (AWS) > Network*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
It is important that VPCs utilizing a Transit Gateway should not have overlapping CIDR. This becomes problematic overtime as the VPCs will likely experience routing issues.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Network
- **Rule ID**: vpcs_in_transit_gateway_no_overlapping_cidr_rule

---

## Remediation
Information on how to fix "VPC's in Transit Gateway should not have common CIDR's" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_vpc resource, set cidr_block argument to use a CIDR block that is not overlapping with other VPC CIDRs using the Transit Gateway.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::EC2::VPC resource, set CidrBlock argument to use a CIDR block that is not overlapping with other VPC CIDRs using the Transit Gateway.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/vpc/latest/userguide/working-with-vpcs.html> to specify a VPC CIDR block that is not overlapping with other VPC CIDRs using the Transit Gateway.




---

## How It Works
Cloudrail will look at all of your Transit Gateways. For each one, it will determine which VPCs are in use. It will iterate over all VPCs in pairs and compare their CIDR blocks. If there's an intersection in the CIDR blocks (one contains an IP that is contained in the other) a violation will be flagged.