# Ensure no human IAM users defined

*Amazon Web Services (AWS) > IAM*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Best practices recommend the use of SSO instead of defining specific users at the account-level.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: IAM
- **Rule ID**: non_car_iam_no_human_users

---

## Remediation
Information on how to fix "Ensure no human IAM users defined" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
Remove the aws_iam_user resource for those identified IAM users.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
Remove the AWS::IAM::User resource for those identified IAM users.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_manage.html#id_users_deleting> to remove identified IAM users.




---

## How It Works
Cloudrail will look at all existing users, and those about to be created, and determine if they are set to be used by humans. This determination is done by looking to see if the user has console access.