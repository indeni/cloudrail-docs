# Ensure RDS instances and clusters have logging enabled

*Amazon Web Services (AWS) > Database*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the RDS instances and clusters configuration in your environment. If an instance or cluster is not configured to export logs to Cloudwatch, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Database
- **Rule ID**: non_car_rds_instance_and_cluster_logging_enabled

---

## Remediation
Information on how to fix "Ensure RDS instances and clusters have logging enabled" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_db_instance or aws_rds_cluster resource, set enabled_cloudwatch_logs_exports argument to a list containing at least one of the supported log types.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::RDS::DBInstance or AWS::RDS::DBCluster resource, set EnableCloudwatchLogsExports argument to a list containing at least one of the supported log types.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch> in order to enable log export to Cloudwatch for RDS instances and clusters.




---

## How It Works
Cloudrail will review the configuration of RDS instances and clusters within your AWS account and Terraform plan to check if Cloudwatch log export is enabled.