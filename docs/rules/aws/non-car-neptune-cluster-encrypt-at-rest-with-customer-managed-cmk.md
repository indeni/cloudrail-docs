# Ensure Neptune clusters being created are set to be encrypted at rest with customer-managed CMK

*Amazon Web Services (AWS) > Database*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the Neptune clusters being created in your environment. If a cluster is not set to encrypt data at rest with a customer-managed CMK, Cloudrail will highlight it as a violation. This rule will only flag a violation for resources that are not yet created.

- **Severity**: 🟢 Low
- **Provider**: Amazon Web Services (AWS)
- **Category**: Database
- **Rule ID**: non_car_neptune_cluster_encrypt_at_rest_with_customer_managed_cmk

---

## Remediation
Information on how to fix "Ensure Neptune clusters being created are set to be encrypted at rest with customer-managed CMK" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_neptune_cluster resource, set storage_encrypted argument to true and set kms_key_arn argument to use a customer-managed CMK.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::Neptune::DBCluster resource, set StorageEncrypted argument to true and set KmsKeyId argument to use a customer-managed CMK.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/neptune/latest/userguide/encrypt.html> to enable encryption at rest using a customer-managed CMK.




---

## How It Works
Cloudrail will identify all Neptune clusters in the Terraform plan that are going to be created and are not configured to encrypt data at rest using a customer-managed CMK.