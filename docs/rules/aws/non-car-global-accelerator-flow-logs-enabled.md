# Ensure Global Accelerator accelerator has flow logs enabled

*Amazon Web Services (AWS) > Network*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review Global Accelerator accelerators configuration in your environment. If an accelerator does not have flow logs enabled, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Network
- **Rule ID**: non_car_global_accelerator_flow_logs_enabled

---

## Remediation
Information on how to fix "Ensure Global Accelerator accelerator has flow logs enabled" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_globalaccelerator_accelerator resource, set the attributes block with flow_logs_enabled argument set to true, flow_logs_s3_bucket argument set to the S3 bucket name, and flow_logs_s3_prefix argument to the prefix used for flow logs.










####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/global-accelerator/latest/dg/monitoring-global-accelerator.flow-logs.html> in order to enable flow logs for an accelerator.




---

## How It Works
Cloudrail will review the configuration of Global Accelerator accelerators within your AWS account and Terraform plan to check if flow logs are enabled.