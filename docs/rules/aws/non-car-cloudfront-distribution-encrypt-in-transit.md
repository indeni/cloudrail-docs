# Ensure CloudFront Distribution being created are set to encrypt in transit

*Amazon Web Services (AWS) > Content Delivery*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the CloudFront Distributions in your environment. If it is not using HTTPS, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Content Delivery
- **Rule ID**: non_car_cloudfront_distribution_encrypt_in_transit

---

## Remediation
Information on how to fix "Ensure CloudFront Distribution being created are set to encrypt in transit" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_cloudfront_distribution resource, in default_cache_behavior/ordered_cache_behavior blocks, set the viewer_protocol_policy argument to https-only or redirect-to-https.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::CloudFront::Distribution resource, in DistributionConfig block and in DefaultCacheBehavior/CacheBehaviors blocks, set ViewerProtocolPolicy to https-only or redirect-to-https.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-viewers-to-cloudfront.html> to enable HTTPS Protocol.




---

## How It Works
Look for CloudFront Distributions, then look inside default_cache_behavior block and ordered_cache_behavior block (can exist several ordered blocks) in order to check the values of: viewer_protocol_policy to ensure it is set to either “https-only” or “redirect-to-https”