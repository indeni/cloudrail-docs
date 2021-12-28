# Ensure ELB has logging enabled

*Amazon Web Services (AWS) > Network*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the Elastic Load Balancers configuration in your environment. If a load balancer does not have logging enabled, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Network
- **Rule ID**: non_car_elb_logging_enabled

---

## Remediation
Information on how to fix "Ensure ELB has logging enabled" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_lb resource, set the access_logs block with enabled argument set to true and the bucket argument set to the S3 bucket name.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::ElasticLoadBalancingV2::LoadBalancer resource, in LoadBalancerAttributes block, add a key-value pair with Key set to "access_logs.s3.enabled" and Value set to true, and add another Key set to "access_logs.s3.bucket" and Value set to the S3 bucket name.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html> or <https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-access-logs.html> in order to enable access logs for the load balancer.




---

## How It Works
Cloudrail will review the Elasticsearch Domains configuration within your AWS account and Terraform plan to check if logging is enabled.