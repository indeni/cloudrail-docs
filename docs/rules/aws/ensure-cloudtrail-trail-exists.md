# Ensure there is at least one trail enabled in Cloudtrail

*Amazon Web Services (AWS) > Logging*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
It is critical to enable Cloudtrail and store it in a bucket for logging and incident response.

- **Severity**: 🔴 Major
- **Provider**: Amazon Web Services (AWS)
- **Category**: Logging
- **Rule ID**: ensure_cloudtrail_trail_exists

---

## Remediation
Information on how to fix "Ensure there is at least one trail enabled in Cloudtrail" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
Create terraform resource aws_cloudtrail and send logs to an S3 bucket.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
Create AWS::CloudTrail::Trail resource and send logs to an S3 bucket.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Go to Cloudtrail and in the Dashboard click on Create trail, make sure multi-region is enabled.




---

## How It Works
Cloudrail will ensure that there is at least one trail enabled in the account.