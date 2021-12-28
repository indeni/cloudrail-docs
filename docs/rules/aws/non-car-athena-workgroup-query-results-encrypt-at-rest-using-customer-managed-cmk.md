# Ensure Athena Workgroup query results being created are set to be encrypted at rest using customer-managed CMKs

*Amazon Web Services (AWS) > Database*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the Athena Workgroups being created in your environment. If a Workgroup is not set to encrypt at rest the query results using customer-managed CMK, Cloudrail will highlight it as a violation. This rule will only flag a violation for resources that are not yet created.

- **Severity**: 🟢 Low
- **Provider**: Amazon Web Services (AWS)
- **Category**: Database
- **Rule ID**: non_car_athena_workgroup_query_results_encrypt_at_rest_using_customer_managed_cmk

---

## Remediation
Information on how to fix "Ensure Athena Workgroup query results being created are set to be encrypted at rest using customer-managed CMKs" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_athena_workgroup resource, in configuration, result_configuration, encryption_configuration block, set the encryption_option argument to "SSE_KMS" and set kms_key_arn argument to use a customer-managed CMK. Additionally, in configuration, set enforce_workgroup_configuration to true.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::Athena::WorkGroup resource, in WorkGroupConfiguration, ResultConfiguration, and EncryptionConfiguration block, set EncryptionOption argument to "SSE_KMS" and set KmsKey argument to use a customer-managed CMK. Additionally, in WorkGroupConfiguration block, set EnforceWorkGroupConfiguration argument to true.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/athena/latest/ug/encrypting-query-results-stored-in-s3.html> to encrypt query results using a customer-managed CMK.




---

## How It Works
Cloudrail will identify all Athena workgroups within your Terraform plan that are going to be created and are encrypting at rest the query results without using customer-managed CMKs.