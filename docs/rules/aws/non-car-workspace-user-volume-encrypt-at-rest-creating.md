# Ensure Workspaces being created are set to encrypt user volume at rest

*Amazon Web Services (AWS) > Compute*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the Workspaces being created in your environment. If a workspace is not set to encrypt user volume at rest, Cloudrail will highlight it as a violation. This rule will only flag a violation for resources that are not yet created.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Compute
- **Rule ID**: non_car_workspace_user_volume_encrypt_at_rest_creating

---

## Remediation
Information on how to fix "Ensure Workspaces being created are set to encrypt user volume at rest" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_workspaces_workspace resource, set the user_volume_encryption_enabled argument to true and set a KMS key in volume_encryption_key argument.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::WorkSpaces::Workspace resource, set UserVolumeEncryptionEnabled argument to true and set a KMS key in VolumeEncryptionKey argument.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/workspaces/latest/adminguide/encrypt-workspaces.html> to encrypt user volumes of Workspaces.




---

## How It Works
Cloudrail will identify all Workspaces in the Terraform plan that are going to be created and are not configured to encrypt user volume at rest.