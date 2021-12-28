# Ensure S3 bucket objects are set to be encrypted at rest

*Amazon Web Services (AWS) > Storage*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the S3 bucket objects being created in your Terraform plan. If a bucket object is not set to encrypt at rest, within a bucket that is not public, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Storage
- **Rule ID**: not_car_s3_bucket_object_encrypt_at_rest

---

## Remediation
Information on how to fix "Ensure S3 bucket objects are set to be encrypted at rest" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_s3_bucket_object resource, set server_side_encryption argument to "AES256".










####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/AmazonS3/latest/user-guide/add-object-encryption.html> to enable S3 bucket object encryption at rest.




---

## How It Works
Cloudrail will identify all S3 objects in the Terraform plan that are going to be created, are not configured to encrypt data at rest and are created in a non-public bucket. Cloudrail will NOT access the S3 objects you already have in your cloud environment. Cloudrail also will not access the contents of the objects in your Terraform plan.