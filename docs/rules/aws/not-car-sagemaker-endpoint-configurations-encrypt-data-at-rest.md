# Ensure Sagemaker endpoint configurations being created are set to be encrypted data at rest

*Amazon Web Services (AWS) > Compute*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the Sagemaker Endpoint Configurations being created in your environment. If a configuration is not set to encrypt data on the storage volume attached to the ML compute instance that hosts the endpoint, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Compute
- **Rule ID**: not_car_sagemaker_endpoint_configurations_encrypt_data_at_rest

---

## Remediation
Information on how to fix "Ensure Sagemaker endpoint configurations being created are set to be encrypted data at rest" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_sagemaker_endpoint_configuration resource, set a key in kms_key_id argument.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::SageMaker::EndpointConfig resource, set a key in KmsKeyId argument.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
In Amazon Sagemaker, Inference, Endpoint configurations, set “Encryption key” to use a key.




---

## How It Works
Cloudrail will identify all Sagemaker Endpoint Configurations in the Terraform plan that are going to be created and are not configured to encrypt data at rest.