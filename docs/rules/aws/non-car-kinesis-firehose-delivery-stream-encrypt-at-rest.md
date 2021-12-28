# Ensure Kinesis Firehose delivery stream are set to be encrypted at rest

*Amazon Web Services (AWS) > Streaming*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the Kinesis firehose delivery stream in your environment. If a stream is not set to encrypt at rest, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Streaming
- **Rule ID**: non_car_kinesis_firehose_delivery_stream_encrypt_at_rest

---

## Remediation
Information on how to fix "Ensure Kinesis Firehose delivery stream are set to be encrypted at rest" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_kinesis_firehose_delivery_stream resource, in server_side_encryption block, set the enable argument to true.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::KinesisFirehose::DeliveryStream resource, in DeliveryStreamEncryptionConfigurationInput block, set KeyType to AWS_OWNED_CMK.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/firehose/latest/dev/create-configure.html> to enable encryption for Kinesis Data Firehose.




---

## How It Works
Cloudrail will identify all Kinesis Firehose delivery streams within your AWS account and Terraform plan that are not configured to be encrypted at rest.