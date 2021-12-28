# Ensure ECR image scanning on push is enabled

*Amazon Web Services (AWS) > Code*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the ECR repositories configuration in your environment. If a repository is not configured to scan images on push, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Code
- **Rule ID**: non_car_ecr_image_scanning_on_push_enabled

---

## Remediation
Information on how to fix "Ensure ECR image scanning on push is enabled" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_ecr_repository resource, in the image_scanning_configuration block, set the scan_on_push parameter to true.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::ECR::Repository resource, in ImageScanningConfiguration block, set ScanOnPush argument to true.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html> to configure image scanning on push for an ECR repository.




---

## How It Works
Cloudrail will review the ECR repositories configuration within your AWS account and Terraform plan to check if image scanning on push is enabled.