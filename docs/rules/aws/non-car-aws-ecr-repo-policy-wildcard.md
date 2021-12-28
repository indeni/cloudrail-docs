# Ensure use of ECR repository policy, and no action wildcards are being used

*Amazon Web Services (AWS) > Code*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Using wildcard actions may inadvertently allow users to take actions you do not want to allow them to do. In addition, using a resource policy will provide an additional layer of security. It is a best practice to use a resource policy and give specific permissions only.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Code
- **Rule ID**: non_car_aws_ecr_repo_policy_wildcard

---

## Remediation
Information on how to fix "Ensure use of ECR repository policy, and no action wildcards are being used" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_ecr_repository_policy resource, modify policy argument in order to avoid using wildcard actions.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::ECR::Repository resource, modify RepositoryPolicyText argument in order to avoid using wildcard actions.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-policies.html> to modify ECR repository policy in order to avoid using wildcard actions.




---

## How It Works
Cloudrail will review the ECR repository policies being created in your environment or currently in use. If a policy is using wildcard actions, or no resource policy configured, Cloudrail will highlight it as a violation.