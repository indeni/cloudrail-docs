# Disallow IAM permissions which can lead to privilege escalation

*Amazon Web Services (AWS) > IAM*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
When setting an IAM policy, one may inadvertently grant a permission which can later be used for privilege escalation. For example, by letting a user attach a policy to IAM entities, they can attach the policy to themselves, and escalate their permissions in the process. Cloudrail will look for policies in use that can create this loophole unintentionally and flag them. Cloudrail will only look at policies that are actually in use.

- **Severity**: 🔴 Major
- **Provider**: Amazon Web Services (AWS)
- **Category**: IAM
- **Rule ID**: iam_priv_escalation_policy

---

## Remediation
Information on how to fix "Disallow IAM permissions which can lead to privilege escalation" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_iam_policy resource, set policy argument to use a policy with proper permissions.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::IAM::Policy resource, set PolicyDocument argument to use a policy with proper permissions.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html> to update the IAM policy permissions.




---

## How It Works
Cloudrail will inspect all of the permissions given to IAM entities and look for permissions that may result in privilege escalation. For example, if an IAM role has iam:AttachRolePolicy, that role can escalate its own permissions by attaching a policy to itself. There are various permissions which can be used to achieve privilege escalation, and Cloudrail will look for them. If any are found, a violation will be flagged with specific information about the problematic permissions.