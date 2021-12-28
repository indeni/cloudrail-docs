# Ensure CloudFront distribution is using WAF

*Amazon Web Services (AWS) > Content Delivery*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the CloudFront distributions in your environment. If a distribution is not using AWS WAF, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Content Delivery
- **Rule ID**: non_car_cloudfront_distribution_using_waf

---

## Remediation
Information on how to fix "Ensure CloudFront distribution is using WAF" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_cloudfront_distribution resource, set the web_acl_id parameter to a WAF Web ACL ARN value.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::CloudFront::Distribution resource, in DistributionConfig block, set WebACLId argument to a WAF Web ACL ARN value.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-awswaf.html> in order to assign an AWS WAF Web ACL to the CloudFront distribution.




---

## How It Works
Cloudrail will review the CloudFront distributions within your AWS account and Terraform plan to check if they are configured to use WAF.