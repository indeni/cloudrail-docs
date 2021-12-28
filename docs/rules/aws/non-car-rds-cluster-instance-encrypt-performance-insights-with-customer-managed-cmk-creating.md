# Ensure RDS cluster instances being created are set to encrypt the performance insights with customer-managed CMK

*Amazon Web Services (AWS) > Database*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the RDS cluster instances being created in your environment. If an RDS cluster instance is not set to encrypt the performance insights with a customer-managed CMK, Cloudrail will highlight it as a violation.

- **Severity**: 🟢 Low
- **Provider**: Amazon Web Services (AWS)
- **Category**: Database
- **Rule ID**: non_car_rds_cluster_instance_encrypt_performance_insights_with_customer_managed_cmk_creating

---

## Remediation
Information on how to fix "Ensure RDS cluster instances being created are set to encrypt the performance insights with customer-managed CMK" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_rds_cluster_instance resource, set performance_insights_kms_key_id argument to use a customer-managed CMK.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::RDS::DBInstance resource, set PerformanceInsightsKMSKeyId argument to use a customer-managed CMK.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.Enabling.html> to enable Performance Insights encryption using a customer-managed CMK.




---

## How It Works
Cloudrail will identify all RDS cluster instances in the Terraform plan that are going to be created and are not configured to encrypt the performance insights using a customer-managed CMK.