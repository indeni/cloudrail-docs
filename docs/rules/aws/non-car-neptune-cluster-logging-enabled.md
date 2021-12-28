# Ensure Neptune cluster has logging enabled

*Amazon Web Services (AWS) > Database*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the Neptune clusters configuration in your environment. If a cluster is not configured to export logs to Cloudwatch, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Database
- **Rule ID**: non_car_neptune_cluster_logging_enabled

---

## Remediation
Information on how to fix "Ensure Neptune cluster has logging enabled" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_neptune_cluster resource, set enable_cloudwatch_logs_exports argument to a list containing the element “audit”.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::Neptune::DBCluster resource, set EnableCloudwatchLogsExports argument to a list containing the element “audit”.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/neptune/latest/userguide/cloudwatch-logs.html> in order to enable log export to Cloudwatch for Neptune cluster.




---

## How It Works
Cloudrail will review the configuration of Neptune clusters within your AWS account and Terraform plan to check if Cloudwatch log export is enabled.