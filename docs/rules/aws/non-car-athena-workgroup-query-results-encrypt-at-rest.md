# Ensure Athena Workgroup query results are set to be encrypted at rest and enforced on clients

*Amazon Web Services (AWS) > Database*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the Athena Workgroups in your environment. If a Workgroup is not set to encrypt at rest the query results, or has it set, but not enforced on the clients, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Database
- **Rule ID**: non_car_athena_workgroup_query_results_encrypt_at_rest

---

## Remediation
Information on how to fix "Ensure Athena Workgroup query results are set to be encrypted at rest and enforced on clients" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_athena_workgroup resource, in configuration, result_configuration, encryption_configuration block, set the encryption_option argument. Additionally, in configuration, set enforce_workgroup_configuration to true.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::Athena::WorkGroup resource, in WorkGroupConfiguration block, ResultConfiguration block, and EncryptionConfiguration block, set EncryptionOption argument to any of the allowed values. Additionally, in WorkGroupConfiguration block, set EnforceWorkGroupConfiguration to true.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/athena/latest/ug/encrypting-query-results-stored-in-s3.html> to encrypt query results.




---

## How It Works
Cloudrail will identify all Athena workgroups within your AWS account and Terraform plan. If the workgroup does not enforce the use of the workgroup config, a violation will be highlighted. If it does, and the config doesn’t have encryption enabled, a violation will be highlighted as well.