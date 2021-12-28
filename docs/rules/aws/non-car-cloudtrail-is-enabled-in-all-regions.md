# Ensure CloudTrail is enabled in all regions

*Amazon Web Services (AWS) > Logging*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the CloudTrail configuration in your environment. If it is not enabled in all regions, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Logging
- **Rule ID**: non_car_cloudtrail_is_enabled_in_all_regions

---

## Remediation
Information on how to fix "Ensure CloudTrail is enabled in all regions" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_cloudtrail resource, set is_multi_region_trail argument to true.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::CloudTrail::Trail resource, set IsMultiRegionTrail argument to true.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.html> to create a trail that logs events in all regions.




---

## How It Works
Cloudrail will review the CloudTrail configuration within your AWS account and Terraform plan to check if it is enabled in all regions.