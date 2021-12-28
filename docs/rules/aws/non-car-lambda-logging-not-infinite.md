# Ensure each Lambda function has a non-infinite log retention

*Amazon Web Services (AWS) > Logging*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
By default, Lambda functions have log groups created for them (either explicitly by the user, or by AWS). It’s important to set a retention period on logs, and not use the default of AWS.

- **Severity**: 🟢 Low
- **Provider**: Amazon Web Services (AWS)
- **Category**: Logging
- **Rule ID**: non_car_lambda_logging_not_infinite

---

## Remediation
Information on how to fix "Ensure each Lambda function has a non-infinite log retention" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
Update the retention_in_days field in the aws_cloudwatch_log_group resource. If you haven't specified one explicitly, create an aws_cloudwatch_log_group resource for the Lambda function as part of the Terraform code.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
Update the RetentionInDays argument in the AWS::Logs::LogGroup resource. If you haven't specified one explicitly, create an AWS::Logs::LogGroup resource for the Lambda function as part of the CloudFormation code.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Find the specific log group for the Lambda function, and change its retention by following <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#SettingLogRetention>.




---

## How It Works
Cloudrail will look through all Lambda functions in both AWS and Terraform. For each function, it will try to find a matching log group, or will assume AWS will create one automatically if a specific one is not provided. It will then review the matching log group’s retention settings.