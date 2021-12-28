# Ensure CloudFront Distribution being created are set to perform field-level encryption

*Amazon Web Services (AWS) > Content Delivery*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the CloudFront Distribution being created in your environment. If it is not using Field Level Encryption, Cloudrail will highlight it as a violation. This rule will only flag a violation for resources that are not yet created.

- **Severity**: 🟢 Low
- **Provider**: Amazon Web Services (AWS)
- **Category**: Content Delivery
- **Rule ID**: non_car_cloudfront_distribution_field_level_encryption_creating

---

## Remediation
Information on how to fix "Ensure CloudFront Distribution being created are set to perform field-level encryption" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_cloudfront_distribution resource, in default_cache_behavior (and/or ordered_cache_behavior) block, set the field_level_encryption_id argument to the Field Level encryption configuration ID.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::CloudFront::Distribution resource, in DistributionConfig, DefaultCacheBehavior/CacheBehaviors blocks, set FieldLevelEncryptionId argument to the Field Level encryption configuration ID.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.html> to enable field-level encryption.




---

## How It Works
Cloudrail will identify all CloudFront distributions in the Terraform plan with cache behavior blocks not configured to perform field-level encryption.