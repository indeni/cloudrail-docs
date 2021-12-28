# Ensure REST API Gateway has access logging enabled

*Amazon Web Services (AWS) > Content Delivery*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the REST API Gateways configuration in your environment. If a stage does not have access logging enabled, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Content Delivery
- **Rule ID**: non_car_rest_api_gateway_access_logging_enabled

---

## Remediation
Information on how to fix "Ensure REST API Gateway has access logging enabled" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_api_gateway_stage resource, set the access_log_settings block with destination_arn argument set to the ARN of a CloudWatch Log Group and set the format argument to a valid log format.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::ApiGateway::Stage resource, in AccessLogSetting block, set DestinationArn to the ARN of a CloudWatch Log Group and set Format argument to a valid log format.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html> in order to enable logging for a REST API Gateway stage.




---

## How It Works
Cloudrail will review the configuration of REST API Gateways within your AWS account and Terraform plan to check if logging is enabled for all stages.