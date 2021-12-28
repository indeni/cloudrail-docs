# Ensure DocDB logging is enabled

*Amazon Web Services (AWS) > Database*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the DocDB clusters configuration in your environment. If a cluster is not configured to export logs to CloudWatch, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Database
- **Rule ID**: non_car_docdb_logging_enabled

---

## Remediation
Information on how to fix "Ensure DocDB logging is enabled" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_docdb_cluster resource, set the enabled_cloudwatch_logs_exports argument to a list containing the values “audit” and “profiler”.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::DocDB::DBCluster resource, set EnableCloudwatchLogsExports argument to a list containing the values “audit” and “profiler”.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/documentdb/latest/developerguide/event-auditing.html> in order to enable audit and profiler logs export to CloudWatch.




---

## How It Works
Cloudrail will review the DocDB clusters configuration within your AWS account and Terraform plan to check if logging is enabled.