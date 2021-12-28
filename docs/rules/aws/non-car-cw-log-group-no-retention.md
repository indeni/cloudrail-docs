# Ensure CloudWatch log groups have a retention policy

*Amazon Web Services (AWS) > Logging*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Having a retention policy on CloudWatch groups is advisable to make sure logs are kept for as long as needed, but not longer. Cloudrail will identify if a retention policy is not set.

- **Severity**: 🟢 Low
- **Provider**: Amazon Web Services (AWS)
- **Category**: Logging
- **Rule ID**: non_car_cw_log_group_no_retention

---

## Remediation
Information on how to fix "Ensure CloudWatch log groups have a retention policy" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_cloudwatch_log_group resource, set the retention_in_days argument to the number of days you want to retain log events.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::Logs::LogGroup resource, set RetentionInDays argument to the number of days you want to retain log events.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html> to set a log data retention policy.




---

## How It Works
Cloudrail will identify all cloudwatch log groups in your AWS account and Terraform plan. For each one, we will look to see if there “retentionInDays” key exists in each of the responses. If this key does not exist, that means there is no retention policy set. This would allow logs to be delivered and stored in this log group forever.