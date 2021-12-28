# Ensure API Gateway has X-Ray tracing enabled

*Amazon Web Services (AWS) > Content Delivery*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review API Gateway stages configuration in your environment. If a stage is not configured to have X-Ray tracing enabled, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Content Delivery
- **Rule ID**: non_car_api_gateway_xray_tracing_enabled

---

## Remediation
Information on how to fix "Ensure API Gateway has X-Ray tracing enabled" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_api_gateway_stage resource, set the xray_tracing_enabled argument to true.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::ApiGateway::Stage resource, set TracingEnabled argument to true.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-enabling-xray.html> in order to enable X-Ray tracing for the API Gateway.




---

## How It Works
Cloudrail will review the API Gateway stages configuration within your AWS account and Terraform plan to check X-Ray tracing is enabled.