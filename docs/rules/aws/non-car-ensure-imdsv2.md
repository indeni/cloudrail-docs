# Ensure IMDSv2 is used and IMDSv1 is disabled

*Amazon Web Services (AWS) > Compute*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
There have been hacks in the past caused by the use of IMDSv1. It is now best practice to disable IMDSv1 and use IMDSv2. It’s important to test the disablement of IMDSv1 carefully, as it may cause issues in an application’s execution (if it using an old SDK, for example).

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Compute
- **Rule ID**: non_car_ensure_imdsv2

---

## Remediation
Information on how to fix "Ensure IMDSv2 is used and IMDSv1 is disabled" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_instance resource, in metadata_options block, set http_tokens argument to required.










####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html> to change the instance metadata for existing instances. Follow the guide at <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html> to configure instance metadata for new instances.




---

## How It Works
Cloudrail will review configurations of EC2 instances, launch configurations, and launch templates used in the environment. If they are set to allow IMDSv1, Cloudrail will highlight it as a violation.