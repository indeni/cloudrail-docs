# Ensure FSx Windows File Systems being created are set to be encrypted at rest using customer-managed CMK

*Amazon Web Services (AWS) > Storage*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the FSx Windows File Systems being created in your environment. If a file system is not set to be encrypted at rest using a customer-managed CMK, Cloudrail will highlight it as a violation.

- **Severity**: 🟢 Low
- **Provider**: Amazon Web Services (AWS)
- **Category**: Storage
- **Rule ID**: non_car_fsx_windows_file_system_encrypted_at_rest_with_customer_managed_cmk

---

## Remediation
Information on how to fix "Ensure FSx Windows File Systems being created are set to be encrypted at rest using customer-managed CMK" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_fsx_windows_file_system resource, set kms_key_id argument to use a customer-managed CMK ARN.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::FSx::FileSystem resource, set KmsKeyId argument to use a customer-managed CMK.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/fsx/latest/WindowsGuide/getting-started-step1.html> to enable file system encryption using a customer-managed CMK.




---

## How It Works
Cloudrail will identify all FSx Windows File Systems in the Terraform plan that are going to be created and are not configured to be encrypted at rest using a customer-managed CMK.