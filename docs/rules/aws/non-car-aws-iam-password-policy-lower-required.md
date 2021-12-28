# Ensure the IAM password policy requires at least one lowercase letter

*Amazon Web Services (AWS) > IAM*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review your AWS account password policy. If your account password policy does not enforce at least one lowercase letter this violation will trigger.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: IAM
- **Rule ID**: non_car_aws_iam_password_policy_lower_required

---

## Remediation
Information on how to fix "Ensure the IAM password policy requires at least one lowercase letter" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_iam_account_password_policy resource, set the require_lowercase_characters argument to true.










####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html#IAMPasswordPolicy> to require at least one lowercase letter.




---

## How It Works
Cloudrail will review your AWS account password policy. If you do not require lowercase characters this rule will trigger. This rule will only run if there is at least one user defined with direct console access (not via SSO).