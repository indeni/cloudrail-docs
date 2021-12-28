# Ensure S3 bucket has access logging enabled

*Amazon Web Services (AWS) > Storage*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the S3 buckets configuration in your environment. If a bucket does not have access logging enabled, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Storage
- **Rule ID**: non_car_s3_bucket_access_logging_enabled

---

## Remediation
Information on how to fix "Ensure S3 bucket has access logging enabled" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_s3_bucket resource, set the logging block with target_bucket argument set to the name of an S3 bucket that will receive the log objects.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::S3::Bucket resource, in LoggingConfiguration block, set DestinationBucketName argument to the name of an S3 bucket that will receive the log objects.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-server-access-logging.html> in order to enable server access logging for an S3 bucket.




---

## How It Works
Cloudrail will review the configuration of S3 buckets within your AWS account and Terraform plan to check if access logging is enabled.