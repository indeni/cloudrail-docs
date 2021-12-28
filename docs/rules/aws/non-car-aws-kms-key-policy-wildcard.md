# Ensure use of KMS key policy, and no action wildcards are being used

*Amazon Web Services (AWS) > Key Management*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Using wildcard actions may inadvertently allow users to take actions you do not want to allow them to do. In addition, using a resource policy will provide an additional layer of security. It is a best practice to use a resource policy and give specific permissions only.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Key Management
- **Rule ID**: non_car_aws_kms_key_policy_wildcard

---

## Remediation
Information on how to fix "Ensure use of KMS key policy, and no action wildcards are being used" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_kms_key resource, modify policy argument in order to avoid using wildcard actions.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::KMS::Key resource, modify KeyPolicy argument in order to avoid using wildcard actions.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html> to modify key policy policy in order to avoid using wildcard actions.




---

## How It Works
Cloudrail will review the KMS keys policies being created in your environment or currently in use. If a policy is using wildcard actions, or no resource policy configured, Cloudrail will highlight it as a violation.