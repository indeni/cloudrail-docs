# Ensure IAM permissions are not given directly to users

*Amazon Web Services (AWS) > IAM*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Best practices dictate that IAM permissions are given to roles, groups, etc., and never directly to users.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: IAM
- **Rule ID**: non_car_iam_no_permissions_directly_to_user

---

## Remediation
Information on how to fix "Ensure IAM permissions are not given directly to users" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
Remove the permission policy attached to the user. Create a new aws_iam_group resource and attach the permission policy. Use the resource aws_iam_user_group_membership for adding the user to the group.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
Remove the permission policy attached to the user. Create a new AWS::IAM::Group resource and attach the permission policy. Use the AWS::IAM::UserToGroupAddition resource for adding the user to the group or modify the AWS::IAM::User Groups argument to add the user to the group.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_create.html> to create an IAM group with the permission policy. Remove the permission policy from the user and follow the guide at to add the IAM user to an IAM group.




---

## How It Works
Cloudrail will review the IAM settings in your environment, and specifically the users being created. If a user is assigned a permission policy directly, Cloudrail will highlight it as a violation.