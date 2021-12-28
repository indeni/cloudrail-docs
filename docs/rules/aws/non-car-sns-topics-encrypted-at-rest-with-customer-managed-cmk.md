# Ensure SNS topics are encrypted at rest with customer-managed CMK

*Amazon Web Services (AWS) > Notifications*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the SNS topics in your environment. If a topic is not set to be encrypted at rest using a customer-managed CMK, Cloudrail will highlight it as a violation.

- **Severity**: 🟢 Low
- **Provider**: Amazon Web Services (AWS)
- **Category**: Notifications
- **Rule ID**: non_car_sns_topics_encrypted_at_rest_with_customer_managed_cmk

---

## Remediation
Information on how to fix "Ensure SNS topics are encrypted at rest with customer-managed CMK" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_sns_topic resource, set kms_master_key_id argument to use a customer-managed CMK.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::SNS::Topic resource, set KmsMasterKeyId argument to use a customer-manager CMK.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/sns/latest/dg/sns-create-topic.html> to enable SNS topic encryption at rest using a customer-managed CMK.




---

## How It Works
Cloudrail will review the SNS topics in your environment. If a topic is not set to be encrypted at rest using a customer-managed CMK, Cloudrail will highlight it as a violation.