# Ensure Elasticsearch Domain has logging enabled

*Amazon Web Services (AWS) > Database*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the Elasticsearch Domains configuration in your environment. If a domain does not have logging enabled, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Database
- **Rule ID**: non_car_elasticsearch_domain_logging_enabled

---

## Remediation
Information on how to fix "Ensure Elasticsearch Domain has logging enabled" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_elasticsearch_domain resource, set the log_publishing_options block with enabled argument set to true, log_type argument set to any of the valid values, and cloudwatch_log_group_arn argument set to the ARN of the CloudWatch Log Group.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::Elasticsearch::Domain resource, in LogPublishingOptions block, add a map for each of the supported types of logs with Enabled argument set to true and CloudWatchLogsLogGroupArn argument set to the ARN of the CloudWatch Log Group.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createdomain-configure-slow-logs.html> in order to configure log publishing for the Elasticsearch domain.




---

## How It Works
Cloudrail will review the Elasticsearch Domains configuration within your AWS account and Terraform plan to check if logging is enabled.