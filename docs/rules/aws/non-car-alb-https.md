# Ensure ALB is using HTTPS and not HTTP

*Amazon Web Services (AWS) > Network*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
In most cases, it is inadvisable to be using HTTP, as confidential or sensitive data may be transported over it, and it’s best to use HTTPS.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Network
- **Rule ID**: non_car_alb_https

---

## Remediation
Information on how to fix "Ensure ALB is using HTTPS and not HTTP" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_lb_listener resource, set protocol argument to HTTPS. Also set ssl_policy and certificate_arn arguments.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::ElasticLoadBalancingV2::Listener resource, set Protocol argument to HTTPS. Also, set SslPolicy argument and in Certificates block, add CertificateArn argument.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-application-load-balancer.html#configure-security-settings> to create a listener that uses HTTPS Protocol.




---

## How It Works
Cloudrail will review the load balancers configured in your environment. If a load balancer is using HTTP, instead of HTTPS, Cloudrail will highlight it as a violation.