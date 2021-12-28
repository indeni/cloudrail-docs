# Ensure CloudTrail trails are set to be encrypted at rest using SSE-KMS

*Amazon Web Services (AWS) > Logging*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the CloudTrail trails in your environment. If a trail is not set to encrypt at rest using SSE-KMS, Cloudrail will highlight it as a violation. This rule will only flag a violation for resources that are not yet created.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Logging
- **Rule ID**: not_car_cloudtrail_trails_encrypt_at_rest_with_sse_kms

---

## Remediation
Information on how to fix "Ensure CloudTrail trails are set to be encrypted at rest using SSE-KMS" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_cloudtrail resource, set kms_key_id argument to use a customer-managed CMK.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::CloudTrail::Trail resource, set KMSKeyId argument to use a customer-managed CMK.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/awscloudtrail/latest/userguide/encrypting-cloudtrail-log-files-with-aws-kms.html> to set encryption at rest using a customer-managed CMK.




---

## How It Works
Cloudrail will identify CloudTrail trails within your AWS account and Terraform plan that are not configured to encrypt at rest using SSE-KMS.