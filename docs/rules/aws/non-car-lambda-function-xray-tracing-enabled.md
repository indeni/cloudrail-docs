# Ensure Lambda function has X-Ray tracing enabled

*Amazon Web Services (AWS) > Compute*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the Lambda functions configuration in your environment. If a function does not have tracing in Active mode, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Compute
- **Rule ID**: non_car_lambda_function_xray_tracing_enabled

---

## Remediation
Information on how to fix "Ensure Lambda function has X-Ray tracing enabled" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_lambda_function resource, set the tracing_config block with mode argument set to “Active”.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::Lambda::Function resource, in TracingConfig block, set Mode argument to “Active”.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/xray/latest/devguide/xray-services-lambda.html> in order to enable X-Ray tracing for a Lambda function.




---

## How It Works
Cloudrail will review the configuration of Lambda functions within your AWS account and Terraform plan to check if X-Ray tracing is enabled.