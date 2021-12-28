# Ensure SQS queues are set to be encrypted at rest

*Amazon Web Services (AWS) > Queuing*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the SQS queues in your environment. If a queue is not set to encrypt at rest, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Queuing
- **Rule ID**: non_car_sqs_queue_encrypt_at_rest

---

## Remediation
Information on how to fix "Ensure SQS queues are set to be encrypted at rest" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the resource aws_sqs_queue, set kms_master_key_id argument to specify a key ID.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::SQS::Queue resource, set KmsMasterKeyId argument to specify a key ID.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-sse-existing-queue.html> to enable encryption at rest for SQS queue.




---

## How It Works
Cloudrail will identify all SQS queues within your AWS account and Terraform plan that are not configured to encrypt data at rest.