# Ensure CloudFront protocol version is a good one

*Amazon Web Services (AWS) > Content Delivery*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
The CloudFront protocol used is an important piece of securing the content flowing between your users and your infrastructure. It's important to use protocol versions that are considered more secure.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Content Delivery
- **Rule ID**: non_car_cloudfront_protocol_version

---

## Remediation
Information on how to fix "Ensure CloudFront protocol version is a good one" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_cloudfront_distribution resource, in viewer_certificate block, set minimum_protocol_version argument to use a secure protocol version.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::CloudFront::Distribution resource, in DistributionConfig and ViewerCertificate block, set MinimumProtocolVersion argument to use a secure protocol version.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValues-security-policy> to configure the Security Policy to use a secure protocol version.




---

## How It Works
Cloudrail will review the CloudFront distributions in your environment. If a CloudFront distribution is using an insecure protocol version (pre TLSv1.2_2019), Cloudrail will highlight it as a violation.