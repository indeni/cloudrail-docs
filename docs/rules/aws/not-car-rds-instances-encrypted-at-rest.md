# Ensure RDS instances/clusters being created are set to be encrypted at rest

*Amazon Web Services (AWS) > Database*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the RDS instances, clusters and global clusters being created in your environment. If an instance, cluster or global cluster is not set to be encrypted at rest, Cloudrail will highlight it as a violation. This rule will only flag a violation for resources that are not yet created.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Database
- **Rule ID**: not_car_rds_instances_encrypted_at_rest

---

## Remediation
Information on how to fix "Ensure RDS instances/clusters being created are set to be encrypted at rest" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_db_instance, aws_rds_global_cluster, and aws_rds_cluster resources, set the storage_encrypted argument to true.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::RDS::Instance, AWS::RDS::GlobalCluster, and AWS::RDS::DBCluster resources, set the StorageEncrypted argument to true.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html> to enable encryption for RDS instances. Follow the guide at <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.CreateInstance.html> to enable encryption for RDS clusters. Follow the guide at <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-getting-started.html> to enable encryption for RDS global clusters.




---

## How It Works
Cloudrail will identify all RDS instances, clusters and global clusters in the Terraform plan that are going to be created and are not configured to be encrypted at rest.