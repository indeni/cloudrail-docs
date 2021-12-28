# Ensure Codebuild report groups being created are set to be encrypted at rest with customer-managed CMK

*Amazon Web Services (AWS) > Code*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the Codebuild report groups in your environment. If a Report Group is not set to encrypt at rest using a customer-managed CMK, Cloudrail will highlight it as a violation.

- **Severity**: 🟢 Low
- **Provider**: Amazon Web Services (AWS)
- **Category**: Code
- **Rule ID**: not_car_codebuild_report_groups_encrypted_at_rest_with_customer_managed_cmk

---

## Remediation
Information on how to fix "Ensure Codebuild report groups being created are set to be encrypted at rest with customer-managed CMK" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_codebuild_report_group resource, in export_config, s3_destination block, set encryption_key argument to use a customer-managed CMK.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::CodeBuild::ReportGroup resource, in ExportConfig, S3Destination block, set EncryptionKey argument to a user a customer-managed CMK.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/codebuild/latest/userguide/test-report-group-create-console.html> to enable report group encryption at rest using a customer-managed CMK.




---

## How It Works
Cloudrail will identify CodeBuild report groups within your AWS account and Terraform plan that are not configured to encrypt at rest using a customer-managed CMK.