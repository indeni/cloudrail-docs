# Allow only private AMIs to be used

*Amazon Web Services (AWS) > Compute*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Some organizations may only allow the use of private AMIs. If this rule is enabled, any EC2 instance attempting to use a public AMI will be flagged.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Compute
- **Rule ID**: non_car_ec2_amis_private_only

---

## Remediation
Information on how to fix "Allow only private AMIs to be used" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_instance resource, update the ami argument to set an approved AMI. Terraform will destroy and create new resources.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::EC2::Instance resource, update the ImageId argument to set an approved AMI.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instances-and-amis.html> in order to terminate flagged EC2 instances and create new EC2 instance with an approved AMI.




---

## How It Works
Cloudrail will look for all EC2 instances in your Terraform plan and live account. For those, it will inspect the AMI ID they are set to use. It will cross reference the ID with the list of AMI IDs that are privately defined in the account or shared with it privately. If it’s not on that list, and it’s not an AMI currently being created by the TF plan, the EC2 resource will be flagged.