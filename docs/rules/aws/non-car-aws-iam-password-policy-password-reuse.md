# Ensure IAM password policy does not allow password re-use

*Amazon Web Services (AWS) > IAM*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review your AWS account password policy. If your account password policy allows users to re-use their previous password this rule will trigger.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: IAM
- **Rule ID**: non_car_aws_iam_password_policy_password_reuse

---

## Remediation
Information on how to fix "Ensure IAM password policy does not allow password re-use" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_iam_account_password_policy resource, set the password_reuse_prevention argument to 24.










####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html#IAMPasswordPolicy> to set Prevent password reuse to 24.




---

## How It Works
Cloudrail will review your AWS account password policy. AWS allows you to set a password reuse prevention between 1-24 This rule will only run if there is at least one user defined with direct console access (not via SSO).