# Ensure SSM Parameter Store SecureString strings are encrypted at rest with customer-managed CMK

*Amazon Web Services (AWS) > Key Management*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the SSM Parameter Store SecureString parameters in your environment. If a SecureString is not set to be encrypted at rest using a customer-managed CMK, Cloudrail will highlight it as a violation. Cloudrail DOES NOT access the contents of the secrets themselves.

- **Severity**: 🟢 Low
- **Provider**: Amazon Web Services (AWS)
- **Category**: Key Management
- **Rule ID**: non_car_ssm_parameter_store_securestring_encrypted_at_rest_with_customer_managed_CMK

---

## Remediation
Information on how to fix "Ensure SSM Parameter Store SecureString strings are encrypted at rest with customer-managed CMK" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_ssm_parameter resource, set key_id argument to a customer-managed CMK ARN.










####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-create-console.html> to provide a customer-managed CMK ARN for the SecureString parameter.




---

## How It Works
Cloudrail will identify SSM Parameter Store SecureString parameters secrets within your AWS account and Terraform plan that are not configured to be encrypted at rest using a customer-managed CMK. Cloudrail DOES NOT access the secret’s contents themselves.