# Ensure API Gateway methods use authentication

*Amazon Web Services (AWS) > Content Delivery*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the API Gateway methods configuration in your environment. If a method is not configured to require authorization, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Content Delivery
- **Rule ID**: non_car_api_gateway_methods_use_authentication

---

## Remediation
Information on how to fix "Ensure API Gateway methods use authentication" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_api_gateway_method resource, set the authorization argument to a value other than “NONE”.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::ApiGateway::Method resource, set the AuthorizationType argument to a value other than “NONE”.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-settings-method-request.html#setup-method-request-authorization> in order to configure the authorization type on the REST API methods.




---

## How It Works
Cloudrail will review the API Gateway methods configuration within your AWS account and Terraform plan to check if authorization has been enabled.