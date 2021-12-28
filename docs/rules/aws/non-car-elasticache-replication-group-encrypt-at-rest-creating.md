# Ensure Elasticache replication groups being created are set to be encrypted at rest

*Amazon Web Services (AWS) > Database*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the Elasticache replication groups being created in your environment. If a replication group is not set to encrypt at rest, Cloudrail will highlight it as a violation. This rule will only flag a violation for resources that are not yet created.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Database
- **Rule ID**: non_car_elasticache_replication_group_encrypt_at_rest_creating

---

## Remediation
Information on how to fix "Ensure Elasticache replication groups being created are set to be encrypted at rest" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_elasticache_replication_group resource, set at_rest_encryption_enabled argument to true.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::ElastiCache::ReplicationGroup resource, set AtRestEncryptionEnabled argument to true.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/at-rest-encryption.html> to enable encryption at rest.




---

## How It Works
Cloudrail will identify all Elasticache replication groups in the Terraform plan that are going to be created and are not configured to be encrypted at rest.