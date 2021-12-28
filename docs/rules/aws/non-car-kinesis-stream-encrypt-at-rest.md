# Ensure Kinesis streams are set to be encrypted at rest

*Amazon Web Services (AWS) > Streaming*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the Kinesis streams in your environment. If a stream is not set to encrypt at rest, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Streaming
- **Rule ID**: non_car_kinesis_stream_encrypt_at_rest

---

## Remediation
Information on how to fix "Ensure Kinesis streams are set to be encrypted at rest" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_kinesis_stream resource, set the encryption_type argument to "KMS" and set kms_key_id argument.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::Kinesis::Stream resource, in StreamEncryption block, set EncryptionType argument to "KMS" and set also KeyId argument.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/streams/latest/dev/getting-started-with-sse.html> to enable encryption for Kinesis streams.




---

## How It Works
Cloudrail will identify all Kinesis streams within your AWS account and Terraform plan that are not configured to be encrypted at rest.