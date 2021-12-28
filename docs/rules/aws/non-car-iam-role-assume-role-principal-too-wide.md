# Ensure no role uses an overly wide principal for assume role policy

*Amazon Web Services (AWS) > IAM*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
When a role is created, a "trust policy" is used to declare who can assume the role. The principal of the trust policy must be specific, and not use the "*" value.

- **Severity**: 🔴 Major
- **Provider**: Amazon Web Services (AWS)
- **Category**: IAM
- **Rule ID**: non_car_iam_role_assume_role_principal_too_wide

---

## Remediation
Information on how to fix "Ensure no role uses an overly wide principal for assume role policy" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
Edit the assume_role_policy under the aws_iam_role, and either make the Principal more specific or add the use of a condition in the policy.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
Edit the AssumeRolePolicyDocument argument under the AWS::IAM::Role, and either make the Principal more specific or add the use of a condition in the policy.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow AWS's guidance on how to write secure IAM role trust policies: <https://aws.amazon.com/blogs/security/how-to-use-trust-policies-with-iam-roles/> iac_remediation_steps: For the aws_sagemaker_endpoint_configuration resource, set kms_key_id argument to a Key ARN.




---

## How It Works
Cloudrail will review all IAM roles in the account. For each one, it will look at the assume role policy to determine if any of the principals are too wide. If a wide principal is found (like "*"), without any conditions, the role will be flagged.