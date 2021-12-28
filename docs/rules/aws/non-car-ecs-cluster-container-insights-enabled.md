# Ensure ECS cluster has container insights enabled

*Amazon Web Services (AWS) > Compute*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the ECS clusters configuration in your environment. If a cluster is not configured to enable container insights, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Compute
- **Rule ID**: non_car_ecs_cluster_container_insights_enabled

---

## Remediation
Information on how to fix "Ensure ECS cluster has container insights enabled" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_ecs_cluster resource, in the setting block, set the name argument to containerInsights and the value argument to enabled.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::ECS::Cluster resource, in ClusterSettings block, set a key-value pair with Key set to "containerInsights" and Valuet set to "enabled".



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/deploy-container-insights-ECS-cluster.html> in order to enable container insights for an ECS cluster.




---

## How It Works
Cloudrail will review the ECS clusters configuration within your AWS account and Terraform plan to check if container insights is enabled.