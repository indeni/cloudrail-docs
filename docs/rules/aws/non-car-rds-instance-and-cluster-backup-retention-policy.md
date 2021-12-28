# Ensure RDS instances and clusters have a backup retention policy

*Amazon Web Services (AWS) > Database*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the RDS instances and clusters configuration in your environment. If an instance or cluster is not configured with a backup retention policy, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Database
- **Rule ID**: non_car_rds_instance_and_cluster_backup_retention_policy

---

## Remediation
Information on how to fix "Ensure RDS instances and clusters have a backup retention policy" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_db_instance or aws_rds_cluster resource, set the backup_retention_period argument to a value higher than 0.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::RDS::DBInstance or AWS::RDS::DBCluster resource, set BackupRetentionPeriod argument to a value higher than 0.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html#USER_WorkingWithAutomatedBackups.BackupRetention> in order to set the backup retention period to a positive nonzero value for RDS instances. Follow the guide at <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Backups.html> in order to set the backup retention period to a positive nonzero value for RDS clusters.




---

## How It Works
Cloudrail will review the RDS instances and clusters within your AWS account and Terraform plan to check if if they have a backup retention policy.