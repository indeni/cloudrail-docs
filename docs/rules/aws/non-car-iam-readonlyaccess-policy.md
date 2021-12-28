# Ensure ReadOnlyAccess policy is not being used by users who can login or roles that can be assumed

*Amazon Web Services (AWS) > IAM*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Some 3rd party vendors may ask for the ReadOnlyAccess policy to be granted. This is now considered a dangerous policy, giving vendors access to confidential S3 bucket contents, secrets, and other sensitive items. This policy should be avoided and Cloudrail will flag its use as a violation.

- **Severity**: 🔴 Major
- **Provider**: Amazon Web Services (AWS)
- **Category**: IAM
- **Rule ID**: non_car_iam_readonlyaccess_policy

---

## Remediation
Information on how to fix "Ensure ReadOnlyAccess policy is not being used by users who can login or roles that can be assumed" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For role: review the aws_iam_role_policy_attachment and switch to a policy that is more restrictive. For user: review aws_iam_user_policy_attachment, and for a group aws_iam_group_policy_attachment.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
Review the Policy argument in AWS::IAM::Role, AWS::IAM::Group, and AWS::IAM::User, and switch to a policy that is more restrictive.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Find the specific user, group or role in the IAM tab and change the policies assigned to it. Choose a more restrictive policy or create a custom one.




---

## How It Works
For each IAM entity, check if it is assigned the ReadOnlyAccess policy. Only look at IAM entities that are either a user with credentials (console login or access keys) or a role with a trust policy (meaning - someone can assume the role). This means you ignore users that no one can login as, or roles that are only internal to the account (can be used by EC2 for example).