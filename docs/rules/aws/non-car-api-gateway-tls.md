# Ensure API Gateway uses modern TLS

*Amazon Web Services (AWS) > Content Delivery*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
It is best to use TLS v1.2 in all encrypted HTTP communications. By default, the API gateway will support TLS v1.0 and v1.1, which should be disabled. If an API Gateway is not set to allow only TLS v1.2, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Content Delivery
- **Rule ID**: non_car_api_gateway_tls

---

## Remediation
Information on how to fix "Ensure API Gateway uses modern TLS" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_api_gateway_domain_name resource, set the argument security_policy argument to "TLS_1_2".








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::ApiGateway::DomainName resource, set SecurityPolicy argument to TLS_1_2.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-custom-domain-tls-version.html> to set a security policy that uses TLS v1.2.




---

## How It Works
Cloudrail will identify all API Gateways within your AWS account and Terraform plan that have a domain configured and allowing TLS v1.0 or v1.1.