# Enforce use of HTTPS in S3 bucket policy

*Amazon Web Services (AWS) > IAM*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Access to objects in S3 should only be done via HTTPS. Blocking HTTP can be done by including a SecureTransport condition in the S3 bucket’s policy.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: IAM
- **Rule ID**: non_car_s3_bucket_policy_secure_transport

---

## Remediation
Information on how to fix "Enforce use of HTTPS in S3 bucket policy" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_s3_bucket_policy resource, ensure the policy denies all actions on the bucket and objects when the request meets the condition (aws:SecureTransport == false).








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::S3::BucketPolicy resource, ensure the policy defined in PolicyDocument argument denies all actions on the bucket and objects when the request meets the condition (aws:SecureTransport == false).



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://aws.amazon.com/premiumsupport/knowledge-center/s3-bucket-policy-for-config-rule/> to create an S3 bucket policy that enforces the use of HTTPS.




---

## How It Works
For each S3 bucket, Cloudrail will look at the policy. If a policy is missing, or there is one but there’s no denial of insecure traffic (aws:SecureTransport == false), a violation will be highlighted.