# Ensure IAM password policy requires at least one number

*Amazon Web Services (AWS) > IAM*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review your AWS account password policy. If your account password policy does not enforce at least one number this violation will trigger.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: IAM
- **Rule ID**: non_car_aws_iam_password_policy_num_required

---

## Remediation
Information on how to fix "Ensure IAM password policy requires at least one number" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_iam_account_password_policy resource, set the require_numbers argument to true.










####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html#IAMPasswordPolicy> to require at least one number.




---

## How It Works
Cloudrail will review your AWS account password policy. If you do not require numbers in this password policy This rule will only run if there is at least one user defined with direct console access (not via SSO).