# Ensure ECR repositories being created are set to be encrypted at rest using customer-managed CMK

*Amazon Web Services (AWS) > Compute*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the ECR repositories being created in your environment. If a repository is not set to be encrypted at rest using a customer-managed CMK, Cloudrail will highlight it as a violation.

- **Severity**: 🟢 Low
- **Provider**: Amazon Web Services (AWS)
- **Category**: Compute
- **Rule ID**: non_car_ecr_repositories_encrypted_at_rest_with_customer_managed_cmk

---

## Remediation
Information on how to fix "Ensure ECR repositories being created are set to be encrypted at rest using customer-managed CMK" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_ecr_repository resource, set kms_key argument, in encryption_configuration block, to use a customer-managed CMK.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::ECR::Repository resource, in EncryptionConfiguration block, set KmsKey argument to use a customer-managed CMK.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/AmazonECR/latest/userguide/encryption-at-rest.html> to create an ECR repository with encryption at rest using a customer-managed CMK.




---

## How It Works
Cloudrail will identify all ECR repositories in the Terraform plan that are going to be created and are not configured to be encrypted at rest using a customer-managed CMK.