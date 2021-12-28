# Cloudrail Rules - Amazon Web Services (AWS)
Cloudrail rules for Amazon Web Services (AWS), click on a rule for more details and how to fix it.

| Severity | Category | Name |
| ----------- | ----------- | ----------- |
 | 🔴 | Compute | [EC2(s) within the public and private subnets should not share identical IAM roles](rules/aws/ec2-role-share-rule) |
 | 🟡 | Network | [VPC's in Transit Gateway should not have common CIDR's](rules/aws/vpcs-in-transit-gateway-no-overlapping-cidr-rule) |
 | 🟡 | Network | [Ensure all used default security groups of every VPC restrict all traffic](rules/aws/ensure-all-used-default-security-groups-restrict-all-traffic-rule) |
 | 🔴 | Compute | [Ensure no used security groups allow ingress from 0.0.0.0/0 or ::/0 to port 22 (SSH)](rules/aws/public-access-security-groups-ssh-port-rule) |
 | 🔴 | Compute | [Ensure no used security groups allow ingress from 0.0.0.0/0 or ::/0 to port 3389 (RDP)](rules/aws/public-access-security-groups-rdp-port-rule) |
 | 🔴 | Compute | [Ensure no used security groups allow ingress from 0.0.0.0/0 or ::/0 to port 1521 (ORACLE DB DEFAULT)](rules/aws/public-access-security-groups-oracle-db-default-port-rule) |
 | 🔴 | Compute | [Ensure no used security groups allow ingress from 0.0.0.0/0 or ::/0 to port 2483 (ORACLE DB)](rules/aws/public-access-security-groups-oracle-db-port-rule) |
 | 🔴 | Compute | [Ensure no used security groups allow ingress from 0.0.0.0/0 or ::/0 to port 2484 (ORACLE DB SSL)](rules/aws/public-access-security-groups-oracle-db-ssl-port-rule) |
 | 🔴 | Compute | [Ensure no used security groups allow ingress from 0.0.0.0/0 or ::/0 to port 3306 (MYSQL)](rules/aws/public-access-security-groups-mysql-port-rule) |
 | 🔴 | Compute | [Ensure no used security groups allow ingress from 0.0.0.0/0 or ::/0 to port 5432 (POSTGRES)](rules/aws/public-access-security-groups-postgres-port-rule) |
 | 🔴 | Compute | [Ensure no used security groups allow ingress from 0.0.0.0/0 or ::/0 to port 6379 (REDIS)](rules/aws/public-access-security-groups-redis-port-rule) |
 | 🔴 | Compute | [Ensure no used security groups allow ingress from 0.0.0.0/0 or ::/0 to port 27017 (MONGODB)](rules/aws/public-access-security-groups-mongodb-port-rule) |
 | 🔴 | Compute | [Ensure no used security groups allow ingress from 0.0.0.0/0 or ::/0 to port 27018 (MONGODB SHARD CLUSTER)](rules/aws/public-access-security-groups-mongodb-shard-cluster-port-rule) |
 | 🔴 | Compute | [Ensure no used security groups allow ingress from 0.0.0.0/0 or ::/0 to port 7199 (CASSANDRA)](rules/aws/public-access-security-groups-cassandra-port-rule) |
 | 🔴 | Compute | [Ensure no used security groups allow ingress from 0.0.0.0/0 or ::/0 to port 9160 (CASSANDRA THRIFT)](rules/aws/public-access-security-groups-cassandra-thrift-port-rule) |
 | 🔴 | Compute | [Ensure no used security groups allow ingress from 0.0.0.0/0 or ::/0 to port 8888 (CASSANDRA MNG)](rules/aws/public-access-security-groups-cassandra-mng-port-rule) |
 | 🔴 | Compute | [Ensure no used security groups allow ingress from 0.0.0.0/0 or ::/0 to port 11211 (MEMCACHED)](rules/aws/public-access-security-groups-memcached-port-rule) |
 | 🔴 | Compute | [Ensure no used security groups allow ingress from 0.0.0.0/0 or ::/0 to port 9300 (ELASTICSEARCH NODES)](rules/aws/public-access-security-groups-elasticsearch-nodes-port-rule) |
 | 🔴 | Compute | [Ensure no used security groups allow ingress from 0.0.0.0/0 or ::/0 to port 9200 (ELASTICSEARCH)](rules/aws/public-access-security-groups-elasticsearch-port-rule) |
 | 🔴 | Compute | [Ensure no used security groups allow ingress from 0.0.0.0/0 or ::/0 to port 5601 (KIBANA)](rules/aws/public-access-security-groups-kibana-port-rule) |
 | 🔴 | Network | [Ensure no used security groups allow ingress from 0.0.0.0/0 or ::/0 to all ports](rules/aws/public-access-security-groups-all-ports-rule) |
 | 🟢 | Compute | [Ensure EC2-Classic mode is not used](rules/aws/disallow-ec2-classic-mode-rule) |
 | 🔴 | Database | [Ensure Redshift database is not publicly accessible](rules/aws/public-access-db-redshift-rule) |
 | 🟡 | Database | [Ensure Redshift database is not accessible indirectly via a publicly accessible resource](rules/aws/indirect-public-access-db-redshift) |
 | 🔴 | Database | [Ensure RDS database is not publicly accessible](rules/aws/public-access-db-rds-rule) |
 | 🟡 | Database | [Ensure RDS instances/clusters being created are set to be encrypted at rest](rules/aws/not-car-rds-instances-encrypted-at-rest) |
 | 🟡 | Compute | [Ensure the default VPC is not used](rules/aws/disallow-default-vpc) |
 | 🟡 | Database | [Ensure RDS database is not accessible indirectly via a publicly accessible resource](rules/aws/indirect-public-access-db-rds) |
 | 🔴 | Database | [Ensure Elasticsearch Domain is not publicly accessible](rules/aws/public-access-elasticsearch-rule) |
 | 🟡 | Database | [Ensure Elasticsearch Domain is not accessible indirectly via a publicly accessible resource](rules/aws/indirect-public-access-elastic-search-rule) |
 | 🟢 | Network | [Ensure used routing tables for VPC peering are "least access"](rules/aws/vpc-peering-least-access) |
 | 🔴 | Database | [Ensure Elasticsearch Domains being created are set to be encrypted at rest](rules/aws/non-car-es-domain-encrypt-at-rest-creating) |
 | 🔴 | Database | [Ensure Elasticsearch domains being created are set to be encrypted node-to-node](rules/aws/not-car-elasticsearch-domains-encrypted-note-to-node) |
 | 🔴 | Kubernetes | [Ensure EKS API is not publicly accessible](rules/aws/public-access-eks-api) |
 | 🟡 | Compute | [Ensure target groups are not using HTTP](rules/aws/non-car-alb-target-group-no-http) |
 | 🔴 | Storage | [Ensure S3 buckets are not made widely accessible through ACLs and bucket policies](rules/aws/s3-acl-disallow-public-and-cross-account) |
 | 🟡 | Content Delivery | [Ensure CloudFront protocol version is a good one](rules/aws/non-car-cloudfront-protocol-version) |
 | 🟡 | IAM | [Ensure IAM permissions are not given directly to users](rules/aws/non-car-iam-no-permissions-directly-to-user) |
 | 🟡 | Compute | [Ensure IMDSv2 is used and IMDSv1 is disabled](rules/aws/non-car-ensure-imdsv2) |
 | 🟡 | Content Delivery | [Ensure CloudFront Distribution being created are set to encrypt in transit](rules/aws/non-car-cloudfront-distribution-encrypt-in-transit) |
 | 🟡 | Notifications | [Ensure SNS topics are set to be encrypted at rest](rules/aws/non-car-sns-topic-encrypt-at-rest) |
 | 🟢 | Notifications | [Ensure SNS topics are encrypted at rest with customer-managed CMK](rules/aws/non-car-sns-topics-encrypted-at-rest-with-customer-managed-cmk) |
 | 🟡 | Queuing | [Ensure SQS queues are set to be encrypted at rest](rules/aws/non-car-sqs-queue-encrypt-at-rest) |
 | 🟡 | Database | [Ensure Athena Workgroup query results are set to be encrypted at rest and enforced on clients](rules/aws/non-car-athena-workgroup-query-results-encrypt-at-rest) |
 | 🟡 | Network | [Ensure ALB is using HTTPS and not HTTP](rules/aws/non-car-alb-https) |
 | 🔴 | Storage | [Ensure VPC Endpoint for S3 is enabled in all VPCs](rules/aws/vpc-endpoint-s3-exposure) |
 | 🔴 | Storage | [Ensure VPC Endpoint for DynamoDB is enabled in all VPCs](rules/aws/vpc-endpoint-dynamodb-exposure) |
 | 🟡 | Content Delivery | [Ensure API Gateway with caching enabled is set to be encrypted](rules/aws/non-car-api-gateway-caching-encrypted) |
 | 🟡 | IAM | [Ensure no human IAM users defined](rules/aws/non-car-iam-no-human-users) |
 | 🟡 | Compute | [Allow only private AMIs to be used](rules/aws/non-car-ec2-amis-private-only) |
 | 🟡 | Database | [Ensure Redshift clusters being created are set to be encrypted at rest](rules/aws/non-car-redshift-cluster-encrypt-at-rest-creating) |
 | 🟡 | Database | [Ensure DocDB clusters being created are set to be encrypted at rest](rules/aws/not-car-docdb-cluster-encrypted-at-rest) |
 | 🟡 | Storage | [Ensure VPC Endpoint for S3 is enabled in all route tables in use in a VPC](rules/aws/endpoint-s3-route-table-exposure) |
 | 🟡 | Storage | [Ensure VPC Endpoint for DynamoDB is enabled in all route tables in use in a VPC](rules/aws/endpoint-dynamodb-route-table-exposure) |
 | 🟡 | Database | [Ensure DynamoDB DAX clusters being created are set to be encrypted at rest](rules/aws/not-car-dynamodb-dax-clusters-encrypted-at-rest) |
 | 🟡 | Service Endpoints, IAM | [Ensure that the private bucket's policy reference a VPC Endpoint as source](rules/aws/s3-bucket-policy-vpce) |
 | 🟢 | Database | [Ensure Athena Workgroup query results being created are set to be encrypted at rest using customer-managed CMKs](rules/aws/non-car-athena-workgroup-query-results-encrypt-at-rest-using-customer-managed-cmk) |
 | 🟡 | Storage | [Ensure S3 buckets are set to be encrypted at rest](rules/aws/not-car-s3-buckets-encrypted-at-rest) |
 | 🟡 | Storage | [Ensure S3 buckets have versioning enabled](rules/aws/not-car-s3-buckets-versioning-enabled) |
 | 🟡 | Storage | [Ensure S3 bucket objects are set to be encrypted at rest](rules/aws/not-car-s3-bucket-object-encrypt-at-rest) |
 | 🟢 | Logging | [Ensure Cloudwatch Log Groups being created are set to be encrypted at rest using KMS CMK](rules/aws/not-car-cloudwatch-log-group-encrypted-at-rest-using-kms-cmk) |
 | 🟢 | Code | [Ensure CodeBuild projects are set to be encrypted at rest with customer-managed CMK](rules/aws/not-car-codebuild-projects-encrypted-at-rest-with-customer-managed-CMK) |
 | 🟡 | Logging | [Ensure CloudTrail trails are set to be encrypted at rest using SSE-KMS](rules/aws/not-car-cloudtrail-trails-encrypt-at-rest-with-sse-kms) |
 | 🟡 | Database | [Ensure Elasticache replication groups being created are set to be encrypted at rest](rules/aws/non-car-elasticache-replication-group-encrypt-at-rest-creating) |
 | 🟡 | Queuing | [Ensure use of SQS queue policy, and no action wildcards are being used](rules/aws/non-car-aws-sqs-policy-wildcard) |
 | 🔴 | Database | [Ensure Elasticache replication groups being created are set to be encrypted in transit](rules/aws/non-car-elasticache-replication-group-encrypt-in-transit-creating) |
 | 🟡 | Database | [Ensure Neptune clusters being created are set to be encrypted at rest](rules/aws/non-car-neptune-cluster-encrypt-at-rest-creating) |
 | 🟢 | Database | [Ensure Neptune clusters being created are set to be encrypted at rest with customer-managed CMK](rules/aws/non-car-neptune-cluster-encrypt-at-rest-with-customer-managed-cmk) |
 | 🟡 | Code | [Ensure use of ECR repository policy, and no action wildcards are being used](rules/aws/non-car-aws-ecr-repo-policy-wildcard) |
 | 🟡 | Storage | [Ensure use of S3 bucket policy, and no action wildcards are being used](rules/aws/non-car-aws-s3-bucket-policy-wildcard) |
 | 🟡 | Key Management | [Ensure use of KMS key policy, and no action wildcards are being used](rules/aws/non-car-aws-kms-key-policy-wildcard) |
 | 🟡 | Content Delivery | [Ensure use of API Gateway endpoint policy, and no action wildcards are being used](rules/aws/non-car-aws-api-gateway-endpoint-policy-wildcard) |
 | 🟡 | Logging | [Ensure use of CloudWatch Logs destination policy, and no action wildcards are being used](rules/aws/non-car-aws-cloudwatch-logs-destination-policy-wildcard) |
 | 🟡 | Database | [Ensure use of Elasticsearch Service domain policy, and no action wildcards are being used](rules/aws/non-car-aws-es-service-domain-policy-wildcard) |
 | 🟡 | Storage | [Ensure use of EFS file system policy, and no action wildcards are being used](rules/aws/non-car-aws-efs-fs-policy-wildcard) |
 | 🟡 | Storage | [Ensure use of S3 Glacier vault policy, and no action wildcards are being used](rules/aws/non-car-aws-glacier-vault-policy-wildcard) |
 | 🟡 | Key Management | [Ensure use of Secrets Manager secret policy, and no action wildcards are being used](rules/aws/non-car-aws-secrets-manager-secret-policy-wildcard) |
 | 🟢 | Key Management | [Ensure Secrets Manager secrets are encrypted at rest with customer-managed CMK](rules/aws/non-car-secrets-manager-secrets-encrypted-at-rest-with-customer-managed-cmk) |
 | 🟡 | Storage | [Ensure use of Glue data catalog policy, and no action wildcards are being used](rules/aws/non-car-aws-glue-data-catalog-policy-wildcard) |
 | 🔴 | Database | [Ensure DocDB clusters are set to encrypt the connection with applications](rules/aws/not-car-docdb-cluster-encrypted-in-transit) |
 | 🟢 | Database | [Ensure SQS queues are encrypted at rest with customer-managed CMK](rules/aws/non-car-sqs-queues-encrypted-at-rest-with-customer-managed-cmk) |
 | 🟢 | Database | [Ensure DocDB clusters being created are set to be encrypted at rest using customer-managed CMK](rules/aws/not-car-docdb-cluster-encrypted-at-rest-using-customer-managed-cmk) |
 | 🔴 | IAM | [Disallow IAM permissions which can lead to privilege escalation](rules/aws/iam-priv-escalation-policy) |
 | 🟡 | Storage | [Ensure EFS filesystems being created are set to be encrypted at rest](rules/aws/non-car-efs-filesystem-encrypt-at-rest-creating) |
 | 🟡 | Content Delivery | [Ensure API Gateway uses modern TLS](rules/aws/non-car-api-gateway-tls) |
 | 🟢 | Content Delivery | [Ensure CloudFront Distribution being created are set to perform field-level encryption](rules/aws/non-car-cloudfront-distribution-field-level-encryption-creating) |
 | 🟡 | Streaming | [Ensure Kinesis streams are set to be encrypted at rest](rules/aws/non-car-kinesis-stream-encrypt-at-rest) |
 | 🟢 | Logging | [Ensure X-Ray encryption config is set to encrypt at rest with customer-managed CMK](rules/aws/non-car-xray-encryption-config-encrypt-at-rest-with-customer-managed-CMK) |
 | 🟡 | Streaming | [Ensure Kinesis Firehose delivery stream are set to be encrypted at rest](rules/aws/non-car-kinesis-firehose-delivery-stream-encrypt-at-rest) |
 | 🟡 | IAM | [Ensure your account password policy expires passwords within 90 days or less](rules/aws/non-car-aws-iam-password-policy-expiry) |
 | 🟡 | IAM | [Ensure the IAM password password policy requires a password of at least 14 characters in length](rules/aws/non-car-aws-iam-password-policy-min-length) |
 | 🟡 | IAM | [Ensure the IAM password policy requires at least one lowercase letter](rules/aws/non-car-aws-iam-password-policy-lower-required) |
 | 🟡 | IAM | [Ensure IAM password policy requires at least one number](rules/aws/non-car-aws-iam-password-policy-num-required) |
 | 🟡 | IAM | [Ensure IAM password policy does not allow password re-use](rules/aws/non-car-aws-iam-password-policy-password-reuse) |
 | 🟡 | IAM | [Ensure the IAM password policy requires at least one symbol](rules/aws/non-car-aws-iam-password-policy-symbol-required) |
 | 🟡 | IAM | [Ensure IAM password policy requires at least one uppercase letter](rules/aws/non-car-aws-iam-password-policy-upper-required) |
 | 🟡 | Compute | [Ensure Workspaces being created are set to encrypt root volume at rest](rules/aws/non-car-workspace-root-volume-encrypt-at-rest-creating) |
 | 🟢 | Compute | [Ensure Workspaces being created are set to encrypt root volume at rest with customer-managed CMK](rules/aws/non-car-workspace-root-volume-encrypt-at-rest-with-customer-managed-CMK-creating) |
 | 🟢 | Compute | [Ensure Workspaces being created are set to encrypt user volume at rest with customer-managed CMK](rules/aws/non-car-workspace-user-volume-encrypt-at-rest-with-customer-managed-cmk-creating) |
 | 🟢 | Code | [Ensure Codebuild report groups being created are set to be encrypted at rest with customer-managed CMK](rules/aws/not-car-codebuild-report-groups-encrypted-at-rest-with-customer-managed-cmk) |
 | 🟡 | Compute | [Ensure Workspaces being created are set to encrypt user volume at rest](rules/aws/non-car-workspace-user-volume-encrypt-at-rest-creating) |
 | 🟡 | IAM | [Enforce use of HTTPS in S3 bucket policy](rules/aws/non-car-s3-bucket-policy-secure-transport) |
 | 🟢 | Logging | [Ensure CloudTrail trails have log validation enabled](rules/aws/non-car-aws-cloudtrail-log-validation-disabled) |
 | 🟢 | Logging | [Ensure CloudWatch log groups have a retention policy](rules/aws/non-car-cw-log-group-no-retention) |
 | 🟢 | Network | [Ensure all security groups and rules have a description detailing the rule](rules/aws/non-car-aws-ec2-security-group-rule-no-desc) |
 | 🟡 | Compute | [Ensure use of Lambda function policy, and no action wildcards are being used](rules/aws/non-car-aws-lambda-func-policy-wildcard) |
 | 🔴 | IAM | [Ensure ReadOnlyAccess policy is not being used by users who can login or roles that can be assumed](rules/aws/non-car-iam-readonlyaccess-policy) |
 | 🔴 | IAM | [Ensure IAM entities policies are managed solely in infrastructure-as-code](rules/aws/car-iam-policy-control-in-iac-only) |
 | 🟡 | Compute | [Ensure ECS task definitions being created are set to encrypt in transit with EFS volumes](rules/aws/non-car-ecs-task-definition-encrypt-in-transit-with-EFS) |
 | 🔴 | Database | [Ensure Neptune database is not publicly accessible](rules/aws/public-access-db-neptune) |
 | 🟢 | Key Management | [Ensure SSM Parameter Store SecureString strings are encrypted at rest with customer-managed CMK](rules/aws/non-car-ssm-parameter-store-securestring-encrypted-at-rest-with-customer-managed-CMK) |
 | 🟡 | Service Endpoints, Queuing | [Ensure VPC Endpoint for SQS is enabled in all VPCs in use](rules/aws/vpc-endpoint-sqs-exposure) |
 | 🟢 | All | [Ensure all resources that can be tagged have at least one tag](rules/aws/non-car-all-resources-tagged) |
 | 🟢 | Logging | [Ensure each Lambda function has a non-infinite log retention](rules/aws/non-car-lambda-logging-not-infinite) |
 | 🟡 | Service Endpoints, Queuing | [Ensure VPC Endpoint for SQS is enabled in all Availability Zones in use a VPC](rules/aws/vpc-endpoint-sqs-subnet-exposure) |
 | 🟡 | Service Endpoints, Queuing | [Ensure VPC Endpoint for EC2 is enabled in all VPCs in use](rules/aws/vpc-endpoint-ec2-exposure) |
 | 🟡 | Compute | [Ensure Sagemaker endpoint configurations being created are set to be encrypted data at rest](rules/aws/not-car-sagemaker-endpoint-configurations-encrypt-data-at-rest) |
 | 🟢 | Compute | [Ensure Sagemaker Notebook instances being created are set to encrypt artifacts at rest with customer-managed CMK](rules/aws/not-car-sagemaker-notebook-instances-encrypt-artifacts-at-rest-with-customer-managed-CMK-creating) |
 | 🔴 | IAM | [Ensure no role uses an overly wide principal for assume role policy](rules/aws/non-car-iam-role-assume-role-principal-too-wide) |
 | 🟢 | Database | [Ensure RDS cluster instances being created are set to encrypt the performance insights with customer-managed CMK](rules/aws/non-car-rds-cluster-instance-encrypt-performance-insights-with-customer-managed-cmk-creating) |
 | 🔴 | Database | [Ensure DMS Replication instance is not publicly accessible](rules/aws/public-access-dms-replication-instance) |
 | 🟡 | IAM | [S3 Bucket is exposed via an overly permissive Lambda Execution Role](rules/aws/s3-lambda-indirect-exposure) |
 | 🟡 | Compute | [Ensure no direct internet access is allowed from Sagemaker Notebook instances](rules/aws/non-car-no-direct-internet-access-allowed-from-sagemaker-notebook-instance-rule) |
 | 🔴 | IAM | [Ensure IAM policies pass Access Analyzer policy validation without SECURITY and ERROR issues](rules/aws/not-car-access-analyzer-validation-error-and-security) |
 | 🟢 | IAM | [Ensure IAM policies pass Access Analyzer policy validation without WARNING and SUGGESTION issues](rules/aws/not-car-access-analyzer-validation-warning-and-suggestion) |
 | 🟡 | Compute | [Ensure no unused Security Group exists in the account](rules/aws/car-unused-security-group) |
 | 🟡 | IAM | [Ensure unused roles are removed](rules/aws/non-car-unused-roles) |
 | 🟡 | Logging | [Ensure CloudTrail is enabled in all regions](rules/aws/non-car-cloudtrail-is-enabled-in-all-regions) |
 | 🟡 | Content Delivery | [Ensure CloudFront distribution is using WAF](rules/aws/non-car-cloudfront-distribution-using-waf) |
 | 🟡 | Network | [Ensure Load Balancer drops invalid HTTP headers](rules/aws/non-car-alb-drops-invalid-http-headers) |
 | 🟢 | Database | [Ensure DynamoDB tables are encrypted at rest with customer-managed CMK](rules/aws/non-car-dynamodb-tables-encrypted-at-rest-with-customer-managed-CMK) |
 | 🟢 | Compute | [Ensure ECR repositories being created are set to be encrypted at rest using customer-managed CMK](rules/aws/non-car-ecr-repositories-encrypted-at-rest-with-customer-managed-cmk) |
 | 🟡 | Code | [Ensure ECR repository image tags are immutable](rules/aws/non-car-ecr-image-tags-immutable) |
 | 🟡 | Database | [Ensure ElastiCache Redis clusters have automatic backup turned on](rules/aws/non-car-elasticache-redis-cluster-automatic-backup-turned-on) |
 | 🟡 | Code | [Ensure ECR image scanning on push is enabled](rules/aws/non-car-ecr-image-scanning-on-push-enabled) |
 | 🟡 | Compute | [Ensure ECS cluster has container insights enabled](rules/aws/non-car-ecs-cluster-container-insights-enabled) |
 | 🟡 | Compute | [Ensure EC2 instance is EBS optimized](rules/aws/non-car-ec2-instance-is-ebs-optimized) |
 | 🟡 | Database | [Ensure RDS instances and clusters have a backup retention policy](rules/aws/non-car-rds-instance-and-cluster-backup-retention-policy) |
 | 🟡 | Content Delivery | [Ensure API Gateway methods use authentication](rules/aws/non-car-api-gateway-methods-use-authentication) |
 | 🟡 | Database | [Ensure RDS database has IAM authentication enabled](rules/aws/non-car-rds-database-iam-authentication-enabled) |
 | 🟡 | Logging | [Ensure Config aggregator is enabled in all regions](rules/aws/non-car-config-aggregator-is-enabled-in-all-regions) |
 | 🟡 | Content Delivery | [Ensure API Gateway has X-Ray tracing enabled](rules/aws/non-car-api-gateway-xray-tracing-enabled) |
 | 🟡 | Content Delivery | [Ensure CloudFront distribution has access logging enabled](rules/aws/non-car-cloudfront-distribution-access-logging-enabled) |
 | 🟡 | Database | [Ensure DocDB logging is enabled](rules/aws/non-car-docdb-logging-enabled) |
 | 🟡 | Compute | [Ensure EC2 instance has detailed monitoring enabled](rules/aws/non-car-ec2-instance-detailed-monitoring-enabled) |
 | 🟡 | Database | [Ensure Elasticsearch Domain has logging enabled](rules/aws/non-car-elasticsearch-domain-logging-enabled) |
 | 🟡 | Network | [Ensure ELB has logging enabled](rules/aws/non-car-elb-logging-enabled) |
 | 🟡 | Network | [Ensure Global Accelerator accelerator has flow logs enabled](rules/aws/non-car-global-accelerator-flow-logs-enabled) |
 | 🟡 | Compute | [Ensure Lambda function has X-Ray tracing enabled](rules/aws/non-car-lambda-function-xray-tracing-enabled) |
 | 🟡 | Database | [Ensure Neptune cluster has logging enabled](rules/aws/non-car-neptune-cluster-logging-enabled) |
 | 🟡 | Database | [Ensure RDS instances and clusters have logging enabled](rules/aws/non-car-rds-instance-and-cluster-logging-enabled) |
 | 🟡 | Database | [Ensure Redshift clusters have logging enabled](rules/aws/non-car-redshift-cluster-logging-enabled) |
 | 🟡 | Content Delivery | [Ensure REST API Gateway has access logging enabled](rules/aws/non-car-rest-api-gateway-access-logging-enabled) |
 | 🟡 | Storage | [Ensure S3 bucket has access logging enabled](rules/aws/non-car-s3-bucket-access-logging-enabled) |
 | 🟡 | Database | [Ensure Athena database is encrypted at rest](rules/aws/non-car-athena-database-encrypted-at-rest) |
 | 🟡 | Compute | [Ensure Lambda functions cannot be invoked by anonymous or all AWS authenticated users](rules/aws/non-car-lambda-public-exposure) |
 | 🟢 | Storage | [Ensure FSx Windows File Systems being created are set to be encrypted at rest using customer-managed CMK](rules/aws/non-car-fsx-windows-file-system-encrypted-at-rest-with-customer-managed-cmk) |
 | 🔴 | Logging | [Ensure there is at least one trail enabled in Cloudtrail](rules/aws/ensure-cloudtrail-trail-exists) |
