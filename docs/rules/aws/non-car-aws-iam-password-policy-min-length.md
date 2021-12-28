# Ensure the IAM password password policy requires a password of at least 14 characters in length

*Amazon Web Services (AWS) > IAM*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review your AWS account password policy. If your accounts password policy allows for passwords under 14 characters, this rule will trigger. This rule will only flag a violation for resources that are not yet created.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: IAM
- **Rule ID**: non_car_aws_iam_password_policy_min_length

---

## Remediation
Information on how to fix "Ensure the IAM password password policy requires a password of at least 14 characters in length" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_iam_account_password_policy resource, set the minimum_password_length argument to at least 14.










####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html#IAMPasswordPolicy> to require a Password minimum length of at least 14 characters.




---

## How It Works
Cloudrail will review your AWS account password policy. This rule checks to ensure your password policy is at least 14 characters in length (longer preferred). This rule will only run if there is at least one user defined with direct console access (not via SSO).