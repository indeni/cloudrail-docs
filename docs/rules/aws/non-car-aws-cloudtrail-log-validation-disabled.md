# Ensure CloudTrail trails have log validation enabled

*Amazon Web Services (AWS) > Logging*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Log validation is important for CloudTrail trails to make sure logs are not invalid nor tampered with. Cloudrail will identify if log validation is not set.

- **Severity**: 🟢 Low
- **Provider**: Amazon Web Services (AWS)
- **Category**: Logging
- **Rule ID**: non_car_aws_cloudtrail_log_validation_disabled

---

## Remediation
Information on how to fix "Ensure CloudTrail trails have log validation enabled" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_cloudtrail resource, set the enable_log_file_validation argument to true.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::CloudTrail::Trail resource, set EnableLogFileValidation argument to true.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-enabling.html> to enable log file integrity validation.




---

## How It Works
Cloudrail will identify all cloudtrail trails within your AWS account. If we detect a trail, we will look to see if log validation is set on the trail, if there is no validation enabled, this rule will fire.