# Ensure your account password policy expires passwords within 90 days or less

*Amazon Web Services (AWS) > IAM*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review your AWS account password policy. If your policy password expire setting is greater than 90 days this rule will trigger. This rule will only flag a violation for resources that are not yet created.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: IAM
- **Rule ID**: non_car_aws_iam_password_policy_expiry

---

## Remediation
Information on how to fix "Ensure your account password policy expires passwords within 90 days or less" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_iam_account_password_policy resource, set the max_password_age argument to 90.










####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html#IAMPasswordPolicy> to require a password expiration of 90 days or less.




---

## How It Works
Cloudrail will review your AWS account password policy. This rule checks to ensure your password policy has a maximum age set This rule will only run if there is at least one user defined with direct console access (not via SSO).