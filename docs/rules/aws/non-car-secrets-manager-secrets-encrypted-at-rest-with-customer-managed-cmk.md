# Ensure Secrets Manager secrets are encrypted at rest with customer-managed CMK

*Amazon Web Services (AWS) > Key Management*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the Secrets Manager secrets config in your environment. If secrets are not set to be encrypted at rest using a customer-managed CMK, Cloudrail will highlight it as a violation. Cloudrail does not access the contents of the secrets themselves.

- **Severity**: 🟢 Low
- **Provider**: Amazon Web Services (AWS)
- **Category**: Key Management
- **Rule ID**: non_car_secrets_manager_secrets_encrypted_at_rest_with_customer_managed_cmk

---

## Remediation
Information on how to fix "Ensure Secrets Manager secrets are encrypted at rest with customer-managed CMK" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_secretsmanager_secret resource, set kms_key_id argument to use a customer-managed CMK.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::SecretsManager::Secret resource, set KmsKeyId argument to use a customer-managed CMK.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/secretsmanager/latest/userguide/tutorials_basic.html> to set encryption at rest using a customer-managed CMK.




---

## How It Works
Cloudrail will identify Secrets Manager secrets within your AWS account and Terraform plan that are not configured to be encrypted at rest using a customer-managed CMK. Cloudrail does not access the secrets contents themselves.