# EC2(s) within the public and private subnets should not share identical IAM roles

*Amazon Web Services (AWS) > Compute*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Having the same IAM role for both public and private instances may be dangerous. Someone may expand the permissions for the role in order to use it in a private workload, not realizing a public workload has the same privileges.

- **Severity**: 🔴 Major
- **Provider**: Amazon Web Services (AWS)
- **Category**: Compute
- **Rule ID**: ec2_role_share_rule

---

## Remediation
Information on how to fix "EC2(s) within the public and private subnets should not share identical IAM roles" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
Create an additional aws_iam_role resource with an aws_iam_role_policy attached. Associate this role to the public EC2 instances using an aws_iam_instance_profile resource.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
Create an additional AWS::IAM::Role resource and AWS::IAM::Policy resource referencing the previous role. Associate this role to the public EC2 instances using AWS::IAM::InstanceProfile resource.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html> to create an additional IAM role with an IAM role policy attached. Associate this role to the public EC2 instances.




---

## How It Works
Cloudrail will iterate over all EC2 resources that use IAM roles. It will classify them between "public" (those that are accessible from the Internet) and "private" (those that are not). If an IAM role is determined to be associated with at least one public instance and at least one private instance, it will be considered in violation.