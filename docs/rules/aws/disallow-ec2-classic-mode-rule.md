# Ensure EC2-Classic mode is not used

*Amazon Web Services (AWS) > Compute*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
AWS accounts created until late 2013 supported EC2 Classic mode. This allowed for an easier configuration of some resources, while having less control over their VPC placement and security. It is not a good practice to continue using EC2 Classic mode.

- **Severity**: 🟢 Low
- **Provider**: Amazon Web Services (AWS)
- **Category**: Compute
- **Rule ID**: disallow_ec2_classic_mode_rule

---

## Remediation
Information on how to fix "Ensure EC2-Classic mode is not used" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
Modify those resources using specific arguments for EC2 Classic only and use VPC mode arguments.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
Modify those resources using specific arguments for EC2 Classic only and use VPC mode arguments.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-migrate.html> to migrate from EC2 Classic mode to VPC mode.




---

## How It Works
Cloudrail will determine if a resource has been configured to use EC2 Classic mode by verifying that the account supports it and the resource does not have a specific VPC set.