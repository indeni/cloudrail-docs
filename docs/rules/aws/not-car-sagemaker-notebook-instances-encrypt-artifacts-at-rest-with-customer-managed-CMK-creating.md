# Ensure Sagemaker Notebook instances being created are set to encrypt artifacts at rest with customer-managed CMK

*Amazon Web Services (AWS) > Compute*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the Sagemaker Notebook instances being created in your environment. If an instance is not set to encrypt artifacts at rest using customer-managed CMK, Cloudrail will highlight it as a violation.

- **Severity**: 🟢 Low
- **Provider**: Amazon Web Services (AWS)
- **Category**: Compute
- **Rule ID**: not_car_sagemaker_notebook_instances_encrypt_artifacts_at_rest_with_customer_managed_CMK_creating

---

## Remediation
Information on how to fix "Ensure Sagemaker Notebook instances being created are set to encrypt artifacts at rest with customer-managed CMK" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_sagemaker_notebook_instance resource, set kms_key_id argument to a customer-managed CMK.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::SageMaker::NotebookInstance resource, set KmsKeyId argument to a customer-managed CMK.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/sagemaker/latest/dg/howitworks-create-ws.html> to enable encryption at rest using a customer-managed CMK.




---

## How It Works
Cloudrail will identify all Sagemaker Notebook instances in the Terraform plan that are going to be created and are not configured to encrypt artifacts at rest using a customer-managed CMK.