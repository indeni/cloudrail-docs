# Ensure API Gateway with caching enabled is set to be encrypted

*Amazon Web Services (AWS) > Content Delivery*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the API Gateways in your environment. If it has caching enabled but not encrypted in any stage and in any method, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Content Delivery
- **Rule ID**: non_car_api_gateway_caching_encrypted

---

## Remediation
Information on how to fix "Ensure API Gateway with caching enabled is set to be encrypted" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_api_gateway_method_settings resource with caching enabled, in settings block, set cache_data_encrypted argument to true.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::ApiGateway::Deployment resource, in StageDescription block, set CacheDataEncrypted argument to true.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html> to encrypt cache data.




---

## How It Works
Cloudrail will identify all API Gateways within your AWS account and Terraform plan that have caching enabled and are not configured to be encrypted at rest.