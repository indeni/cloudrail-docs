# Ensure SNS topics are set to be encrypted at rest

*Amazon Web Services (AWS) > Notifications*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the SNS topics in your environment. If a topic is not set to encrypt at rest, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Notifications
- **Rule ID**: non_car_sns_topic_encrypt_at_rest

---

## Remediation
Information on how to fix "Ensure SNS topics are set to be encrypted at rest" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the resource aws_sns_topic, set kms_master_key_id argument to specify a key ID.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::SNS::Topic resource, set KmsMasterKeyId argument to specify a key ID.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/sns/latest/dg/sns-create-topic.html> to enable encryption at rest for SNS topic.




---

## How It Works
Cloudrail will identify all SNS topics within your AWS account and Terraform plan that are not configured to encrypt data at rest.