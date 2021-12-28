# Ensure EFS filesystems being created are set to be encrypted at rest

*Amazon Web Services (AWS) > Storage*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the EFS filesystems being created in your environment. If a filesystem is not set to encrypt at rest, Cloudrail will highlight it as a violation. This rule will only flag a violation for resources that are not yet created.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Storage
- **Rule ID**: non_car_efs_filesystem_encrypt_at_rest_creating

---

## Remediation
Information on how to fix "Ensure EFS filesystems being created are set to be encrypted at rest" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_efs_file_system resource, set encrypted argument to true.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::EFS::FileSystem resource, set Encrypted argument to true.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/efs/latest/ug/encryption-at-rest.html> to enable encryption at rest for EFS filesystems.




---

## How It Works
Cloudrail will identify all EFS filesystems in the Terraform plan that are going to be created and are not configured to be encrypted at rest.