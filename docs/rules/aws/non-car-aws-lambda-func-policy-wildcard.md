# Ensure use of Lambda function policy, and no action wildcards are being used

*Amazon Web Services (AWS) > Compute*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Using wildcard actions may inadvertently allow users to take actions you do not want to allow them to do. It is a best practice to give specific permissions only.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Compute
- **Rule ID**: non_car_aws_lambda_func_policy_wildcard

---

## Remediation
Information on how to fix "Ensure use of Lambda function policy, and no action wildcards are being used" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_lambda_permission resource, modify policy argument in order to avoid using wildcard actions.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::Lambda::Permission resource, modify Action argument in order to avoid using wildcard actions.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html> to modify Lambda function policy in order to avoid using wildcard actions.




---

## How It Works
Cloudrail will review the Lambda function policies being created in your environment or currently in use. If a policy is using wildcard actions, Cloudrail will highlight it as a violation.