# Ensure target groups are not using HTTP

*Amazon Web Services (AWS) > Compute*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Best practices encourage encryption of communication between each two entities in your environment. This includes between a load balancer and the servers it is connected to.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Compute
- **Rule ID**: non_car_alb_target_group_no_http

---

## Remediation
Information on how to fix "Ensure target groups are not using HTTP" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_lb_target_group resource, set the protocol argument to use HTTPS.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::ElasticLoadBalancingV2::TargetGroup resource, set the Protocol argument to HTTPS.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-target-group.html> to configure HTTPS Protocol.




---

## How It Works
Cloudrail will review the load balancers and target groups configured in your environment. If a target group is in use and is communicating with its targets in HTTP, Cloudrail will flag a violation.