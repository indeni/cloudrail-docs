# Ensure Cloudwatch Log Groups being created are set to be encrypted at rest using KMS CMK

*Amazon Web Services (AWS) > Logging*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the Cloudwatch Log Groups being created in your environment. If a Log Group is not set to encrypt at rest using KMS CMK, Cloudrail will highlight it as a violation. This rule will only flag a violation for resources that are not yet created.

- **Severity**: 🟢 Low
- **Provider**: Amazon Web Services (AWS)
- **Category**: Logging
- **Rule ID**: not_car_cloudwatch_log_group_encrypted_at_rest_using_kms_cmk

---

## Remediation
Information on how to fix "Ensure Cloudwatch Log Groups being created are set to be encrypted at rest using KMS CMK" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_cloudwatch_log_group resource, set kms_key_id argument to use a customer-managed CMK.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::Logs::LogGroup resource, set KmsKeyId argument to use a customer-managed CMK.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/encrypt-log-data-kms.html> to set encryption at rest using a customer-managed CMK.




---

## How It Works
Cloudrail will identify all Cloudwatch Log Groups in the Terraform plan that are going to be created and are not configured to encrypt data at rest.