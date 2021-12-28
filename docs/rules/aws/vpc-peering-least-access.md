# Ensure used routing tables for VPC peering are "least access"

*Amazon Web Services (AWS) > Network*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
It's important to ensure that only specific networks are exposed through a VPC peering connection. Exposing an entire VPC through the connection may create the risk of exposing resources that were not intended.

- **Severity**: 🟢 Low
- **Provider**: Amazon Web Services (AWS)
- **Category**: Network
- **Rule ID**: vpc_peering_least_access

---

## Remediation
Information on how to fix "Ensure used routing tables for VPC peering are "least access"" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_route resource, set destination_cidr_block argument to use specific routes for VPC peering.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::EC2::Route resource, set DestinationCidrBlock argument to use specific routes for VPC peering.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/vpc/latest/peering/peering-configurations-partial-access.html> to configure specific routes for VPC peering.




---

## How It Works
Cloudrail will review all of the routing tables configured in your environment that have routes pointing to a VPC peer. It will then cross reference these routing tables with the subnets they are attached to, and with the resources they are used with, to determine they are used at all. For those routing tables that are used, Cloudrail will review the routes defined and cross-reference them with the VPC’s CIDR block. If a route is found to exactly match the CIDR block, it will be highlighted by Cloudrail. By doing this context-based analysis, Cloudrail ensures that only routing tables who pose a true security risk are highlighted. NOTE: If a VPC Peering Connection is created through Terraform, to a VPC in a different account, Cloudrail will only be able to evaluate this rule after the connection has been established. This is due to the lack of knowledge of the peer VPC’s CIDR block.