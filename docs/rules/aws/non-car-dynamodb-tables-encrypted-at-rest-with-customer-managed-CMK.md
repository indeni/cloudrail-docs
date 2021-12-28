# Ensure DynamoDB tables are encrypted at rest with customer-managed CMK

*Amazon Web Services (AWS) > Database*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the DynamoDB tables in your environment. If a table is not set to be encrypted at rest using a customer-managed CMK, Cloudrail will highlight it as a violation.

- **Severity**: 🟢 Low
- **Provider**: Amazon Web Services (AWS)
- **Category**: Database
- **Rule ID**: non_car_dynamodb_tables_encrypted_at_rest_with_customer_managed_CMK

---

## Remediation
Information on how to fix "Ensure DynamoDB tables are encrypted at rest with customer-managed CMK" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_dynamodb_table resource, set kms_key_arn argument, in server_side_encryption block, to use a customer-managed CMK.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::DynamoDB::Table resource, in SSESpecification block, set KMSMasterKeyId argument to use a customer-managed CMK.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/encryption.tutorial.html> to set DynamoDB table encryption using a customer-managed CMK.




---

## How It Works
Cloudrail will identify DynamoDB tables within your AWS account and Terraform plan that are not configured to be encrypted at rest using a customer-managed CMK.