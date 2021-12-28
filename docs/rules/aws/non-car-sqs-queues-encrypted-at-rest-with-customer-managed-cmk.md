# Ensure SQS queues are encrypted at rest with customer-managed CMK

*Amazon Web Services (AWS) > Database*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the SQS queues in your environment. If a queue is not set to be encrypted at rest using a customer-managed CMK, Cloudrail will highlight it as a violation.

- **Severity**: 🟢 Low
- **Provider**: Amazon Web Services (AWS)
- **Category**: Database
- **Rule ID**: non_car_sqs_queues_encrypted_at_rest_with_customer_managed_cmk

---

## Remediation
Information on how to fix "Ensure SQS queues are encrypted at rest with customer-managed CMK" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_sqs_queue resource, set the argument kms_master_key_id to use a customer-managed CMK.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::SQS::Queue resource, set the KmsMasterKeyId argument to use a customer-managed CMK.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-sse-existing-queue.html> to enable encryption at rest using a customer-managed CMK.




---

## How It Works
Cloudrail will identify SQS queues within your AWS account and Terraform plan that are not configured to be encrypted at rest using a customer-managed CMK.