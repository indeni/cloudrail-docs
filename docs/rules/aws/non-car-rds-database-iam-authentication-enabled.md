# Ensure RDS database has IAM authentication enabled

*Amazon Web Services (AWS) > Database*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review RDS instances and clusters configuration in your environment. If IAM authentication is not enabled, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Database
- **Rule ID**: non_car_rds_database_iam_authentication_enabled

---

## Remediation
Information on how to fix "Ensure RDS database has IAM authentication enabled" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_db_instance or aws_rds_cluster resources, set the iam_database_authentication_enabled argument to true.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::RDS::DBInstance or AWS::RDS::DBCluster resource, set EnableIAMDatabaseAuthentication argument to true.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.Enabling.html> in order to enable IAM database authentication for the RDS instance or cluster.




---

## How It Works
Cloudrail will review the configuration of RDS instances and clusters within your AWS account and Terraform plan to check if IAM authentication is enabled.