# Ensure ECS task definitions being created are set to encrypt in transit with EFS volumes

*Amazon Web Services (AWS) > Compute*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the ECS task definitions being created in your environment. If a task definition is not set to encrypt in transit with EFS volumes, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Compute
- **Rule ID**: non_car_ecs_task_definition_encrypt_in_transit_with_EFS

---

## Remediation
Information on how to fix "Ensure ECS task definitions being created are set to encrypt in transit with EFS volumes" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_ecs_task_definition resource, in volume, efs_volume_configuration block, set transit_encryption argument to ENABLED.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::ECS::TaskDefinition resource, in Volumes, EFSVolumeConfiguration block, set TransitEncryption argument to ENABLED.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/efs-volumes.html> to enable encryption for Amazon EFS data in transit between ECS host and EFS server.




---

## How It Works
Cloudrail will identify all ECS task definitions in the Terraform plan. It will check if the task definition is using an EFS volume, and if so, it will check if it is enabled to perform encryption in transit.