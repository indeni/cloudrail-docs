# Ensure IAM entities policies are managed solely in infrastructure-as-code

*Amazon Web Services (AWS) > IAM*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
When defining a new IAM entity in infrastructure-as-code (such as Terraform), and assigning policies to it in the same set of code, a user has the expectation that no other policies will be assigned to the same entity through other means. For example, a user’s expectation is that no one will assign an additional policy to the same entity through the AWS console. This rule allows you to ensure that indeed, policy assignment to an IAM entity created in infrastructure-as-code is only done via infrastructure-as-code, and not external means. Thereby ensuring that the IAM entity only has the permissions declared for it in the code.

- **Severity**: 🔴 Major
- **Provider**: Amazon Web Services (AWS)
- **Category**: IAM
- **Rule ID**: car_iam_policy_control_in_iac_only

---

## Remediation
Information on how to fix "Ensure IAM entities policies are managed solely in infrastructure-as-code" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
Consider updating the code to reflect the policy attachments that were not originally done through the Terraform code. Adding the needed aws_iam_<user|role|group>_policy_attachment resources that are missing would resolve this.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
Consider updating the code to reflect the policy attachments that were not originally done through the CloudFormation code. Adding the needed policies to Policies argument in AWS::IAM::<User|Group|Role> resources.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Find the IAM entity within the AWS console and remove any policies attached that were not added originally through the infrastructure-as-code.




---

## How It Works
Cloudrail will review all IAM entities (role, user, group) created through Terraform and that have at least one policy attached via the Terraform code. For each entity, it will determine if there are additional policies attached to it, not through the Terraform code. For example, a policy attachment done in the AWS console directly. If such a case occurs, a violation will be flagged.