# Ensure Redshift clusters have logging enabled

*Amazon Web Services (AWS) > Database*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the Redshift clusters configuration in your environment. If a cluster does not have logging enabled, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Database
- **Rule ID**: non_car_redshift_cluster_logging_enabled

---

## Remediation
Information on how to fix "Ensure Redshift clusters have logging enabled" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_redshift_cluster resource, set the logging block with enable argument set to true and bucket_name argument to the S3 bucket name to store the logs.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::Redshift::Cluster resource, in LoggingProperties block, set BucketName argument to the S3 bucket name to store the logs.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/redshift/latest/mgmt/db-auditing.html> in order to enable logging to an S3 bucket.




---

## How It Works
Cloudrail will review the configuration of Redshift clusters within your AWS account and Terraform plan to check if logging is enabled.