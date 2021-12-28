# Ensure the default VPC is not used

*Amazon Web Services (AWS) > Compute*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Many AWS resources can be configured to reside in a specific VPC. If parameters are left to their default values, AWS may place the resource in the default VPC. This isn’t a good practice, as it’s best to specifically configure such parameters. Cloudrail will determine if resources are placed in the default VPC.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Compute
- **Rule ID**: disallow_default_vpc

---

## Remediation
Information on how to fix "Ensure the default VPC is not used" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
Create aws_security_group resources for those AWS resources using default VPC security group.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
Create AWS::EC2::SecurityGroup resources for those AWS resources using default VPC security group.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html> to create specific Security Groups for those resources.




---

## How It Works
Cloudrail will review all resources configured to determine if any of them is set to use the default VPC. This includes resources that may have no VPC ID set and would be assigned the default VPC upon creation.