# Ensure Athena database is encrypted at rest

*Amazon Web Services (AWS) > Database*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the Athena database configuration. If a database is not configured to be encrypted at rest, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Database
- **Rule ID**: non_car_athena_database_encrypted_at_rest

---

## Remediation
Information on how to fix "Ensure Athena database is encrypted at rest" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_athena_database resource, set the encryption_configuration block with the encryption_option argument set to either “SSE_S3”, “SSE_KMS”, or “CSE_KMS”.










####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/athena/latest/ug/creating-tables-based-on-encrypted-datasets-in-s3.html> in order to encrypt the Athena database.




---

## How It Works
Cloudrail will review the Athena databases configuration in your Terraform plan to check if encryption at rest is enabled.