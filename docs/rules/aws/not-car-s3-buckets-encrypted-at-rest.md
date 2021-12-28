# Ensure S3 buckets are set to be encrypted at rest

*Amazon Web Services (AWS) > Storage*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the S3 buckets in your environment. If an S3 bucket is not set to be encrypted at rest, and the bucket is not public, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Storage
- **Rule ID**: not_car_s3_buckets_encrypted_at_rest

---

## Remediation
Information on how to fix "Ensure S3 buckets are set to be encrypted at rest" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_s3_bucket resource, in server_side_encryption_configuration, rule, apply_server_side_encryption_by_default block, set sse_algorithm argument to an allowed value.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::S3::Bucket resource, in BucketEncryption, ServerSideEncryptionConfiguration, and ServerSideEncryptionByDefault block, set the SSEAlgorithm argument to an allowed value.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html> to enable S3 bucket encryption at rest.




---

## How It Works
Cloudrail will identify all S3 buckets within your AWS account and Terraform plan that are not configured to encrypt data at rest and are not public.