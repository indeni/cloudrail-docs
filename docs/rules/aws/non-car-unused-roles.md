# Ensure unused roles are removed

*Amazon Web Services (AWS) > IAM*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Roles should be maintained carefully, in order to provide access for desired entities. Having unused Roles may leave open a door to bad actors.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: IAM
- **Rule ID**: non_car_unused_roles

---

## Remediation
Information on how to fix "Ensure unused roles are removed" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
Remove the unused aws_iam_role resource from your TF template.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
Remove the unused AWS::IAM::Role resource from your CFN template.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Delete the unusued IAM Roles from your AWS Console.




---

## How It Works
Cloudrail will review all of the IAM Roles in your environment. It will utilize AWS's role usage tracking to determine when the role was used last. If it wasn't used in over 90 days, or was created over 90 days ago and never used, Cloudrail will highlight a violation.