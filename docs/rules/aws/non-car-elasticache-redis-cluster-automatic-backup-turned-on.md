# Ensure ElastiCache Redis clusters have automatic backup turned on

*Amazon Web Services (AWS) > Database*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the ElastiCache Redis clusters configuration in your environment. If a Redis cluster has automatic backup turned off, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Database
- **Rule ID**: non_car_elasticache_redis_cluster_automatic_backup_turned_on

---

## Remediation
Information on how to fix "Ensure ElastiCache Redis clusters have automatic backup turned on" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_elasticache_cluster resource, set the snapshot_retention_limit argument to a value higher than 0.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::ElastiCache::CacheCluster resource, set SnapshotRetentionLimit argument to a value higher than 0.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/backups-automatic.html> in order to enable automatic backups for a ElastiCache Redis cluster.




---

## How It Works
Cloudrail will review the ElastiCache Redis clusters within your AWS account and Terraform plan to check if if they have automatic backup turned on.