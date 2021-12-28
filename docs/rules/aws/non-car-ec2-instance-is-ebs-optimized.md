# Ensure EC2 instance is EBS optimized

*Amazon Web Services (AWS) > Compute*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the EC2 instances configuration in your environment. If it is not configured to be EBS-optimized, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Compute
- **Rule ID**: non_car_ec2_instance_is_ebs_optimized

---

## Remediation
Information on how to fix "Ensure EC2 instance is EBS optimized" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_instance resource, set the ebs_optimized parameter to true.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::EC2::Instance resource, set EbsOptimized argument to true.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html> to enable EBS optimization for an EC2 instance.




---

## How It Works
Cloudrail will review the EC2 instances configuration within your AWS account and Terraform plan to check if it is configured to be EBS optimized.