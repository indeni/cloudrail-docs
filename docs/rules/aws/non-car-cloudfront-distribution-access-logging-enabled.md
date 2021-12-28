# Ensure CloudFront distribution has access logging enabled

*Amazon Web Services (AWS) > Content Delivery*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the CloudFront distributions configuration in your environment. If a distribution has access logging disabled, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Content Delivery
- **Rule ID**: non_car_cloudfront_distribution_access_logging_enabled

---

## Remediation
Information on how to fix "Ensure CloudFront distribution has access logging enabled" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_cloudfront_distribution resource, configure the logging_config block with bucket argument set to the S3 bucket name for storing access logs.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::CloudFront::Distribution resource, in DistributionConfig, Logging block, set Bucket argument to the S3 bucket name for storing access logs.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html> in order to enabled access logs for the CloudFront distribution.




---

## How It Works
Cloudrail will review the CloudFront distributions configuration within your AWS account and Terraform plan to check if access logging is enabled.