# Ensure no unused Security Group exists in the account

*Amazon Web Services (AWS) > Compute*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Security Groups should be maintained carefully, in order to provide network access for desired entities. Having unused Security Groups is giving the oppertunity to accidently assign vulnerbale network access to your resources.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Compute
- **Rule ID**: car_unused_security_group

---

## Remediation
Information on how to fix "Ensure no unused Security Group exists in the account" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
Remove the unused aws_security_group resource from your TF template.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
Remove the unused AWS::EC2::SecurityGroup resource from your CFN template.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Delete the unusued Security Group from your AWS Console.




---

## How It Works
Cloudrail will review all of the Network interfaces in your environment, and your Security Groups. Cloudrail will create a list of all used Security Groups, based on the Network interfaces in your environment, which are attached to AWS resources. It will then compare this list to the actual Security Groups in the account. For a Security Group which is present, but not used by any attached Network interface, Cloudrail will raise a violation.