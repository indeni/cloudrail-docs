# Ensure S3 buckets have versioning enabled

*Amazon Web Services (AWS) > Storage*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Using versioning is a good practice to deal with accidental deletion or modifications. Cloudrail will review your buckets to ensure versioning is enabled. This rule is not context aware

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Storage
- **Rule ID**: not_car_s3_buckets_versioning_enabled

---

## Remediation
Information on how to fix "Ensure S3 buckets have versioning enabled" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_s3_bucket resource, in versioning block, set enabled argument to true.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::S3::Bucket resource, in VersioningConfiguration block, set Status argument to Enabled.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/AmazonS3/latest/userguide/manage-versioning-examples.html> to enable S3 bucket versioning.




---

## How It Works
Cloudrail will review all S3 buckets within your AWS account and Terraform plan. If versioning is not enabled, this rule will trigger.