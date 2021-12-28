# Ensure Lambda functions cannot be invoked by anonymous or all AWS authenticated users

*Amazon Web Services (AWS) > Compute*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Broad permissions in a Lambda function are dangerous and also are potentially expensive as anyone can invoke the function. Best practices suggest use the approach of least privilege. Generally, the correct approach is not to use public Lambda functions but to put them behind an API Gateway.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Compute
- **Rule ID**: non_car_lambda_public_exposure

---

## Remediation
Information on how to fix "Ensure Lambda functions cannot be invoked by anonymous or all AWS authenticated users" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
In resource aws_lambda_permission avoid using wildcards in the principal.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
In resource AWS::Lambda::Permission avoid using wildcards in Principal argument.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the steps in <https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html#permissions-resource-serviceinvoke> Avoid using wildcards in the principal.




---

## How It Works
Cloudrail will review all Lambda functions, both those defined in the AWS account, and those included in a Terraform plan, to determine if any of the permissions they grant include a “*” or similar principal who can InvokeFunction.