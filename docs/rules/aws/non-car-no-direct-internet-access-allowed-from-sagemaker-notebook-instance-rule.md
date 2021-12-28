# Ensure no direct internet access is allowed from Sagemaker Notebook instances

*Amazon Web Services (AWS) > Compute*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the Sagemaker Notebook instances in your environment. If an instance uses direct internet access, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Compute
- **Rule ID**: non_car_no_direct_internet_access_allowed_from_sagemaker_notebook_instance_rule

---

## Remediation
Information on how to fix "Ensure no direct internet access is allowed from Sagemaker Notebook instances" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_sagemaker_notebook_instance resource, set direct_internet_access argument to "Disabled", and add subnet_id and security_groups arguments for the resource.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::SageMaker::NotebookInstance resource, set DirectInternetAccess argument to "Disabled", and add SubnetId and SecurityGroupIds arguments for the resource.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/sagemaker/latest/dg/appendix-notebook-and-internet-access.html> to configure your instance with some VPC, and disable the "direct internet access" option while creating the Sagemaker Notebook instance.




---

## How It Works
Cloudrail will identify all Sagemaker Notebook instances which use direct internet access.