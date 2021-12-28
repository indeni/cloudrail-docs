# Ensure all security groups and rules have a description detailing the rule

*Amazon Web Services (AWS) > Network*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review your security groups. If a security group is using a default description, or has a rule which does not include a description, this rule will trigger.

- **Severity**: 🟢 Low
- **Provider**: Amazon Web Services (AWS)
- **Category**: Network
- **Rule ID**: non_car_aws_ec2_security_group_rule_no_desc

---

## Remediation
Information on how to fix "Ensure all security groups and rules have a description detailing the rule" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_security_group and aws_security_group_rule resources, set description argument with a proper value. Note, this will force the re-creation of the security group and all resources that depend on it. This is an AWS limitation.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::EC2::SecurityGroup, AWS::EC2::SecurityGroupEgress, and AWS::EC2::SecurityGroupIngress resources, set Description argument with a proper value.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html> to update the security group or security group rules description field.




---

## How It Works
Cloudrail will review all security groups within your AWS account. If we find a security group we will check to see if it has a non-default description (for example, “Managed by Terraform” is considered default). If there’s a default description, this rule will trigger. In addition, Cloudrail will check that each inbound rule contains a description, if there is no description this rule will trigger. We will also check all outbound rules. If we find an outbound rule that does not have a target CIDR of ‘`0.0.0.0/0`’ (default), we will check to see if there is no description set. If there is no description, this rule will trigger.