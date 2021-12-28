# Ensure Load Balancer drops invalid HTTP headers

*Amazon Web Services (AWS) > Network*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the Load Balancers in your environment. If a Load Balancer is not set drop invalid HTTP headers, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Network
- **Rule ID**: non_car_alb_drops_invalid_http_headers

---

## Remediation
Information on how to fix "Ensure Load Balancer drops invalid HTTP headers" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_lb resource, set the drop_invalid_header_fields parameter to true.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::ElasticLoadBalancingV2::LoadBalancer resource, in LoadBalancerAttribute block, add a key-value pair with Key set to "routing.http.drop_invalid_header_fields.enabled" and Value set to true.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html> to enable the Drop invalid header fields parameter.




---

## How It Works
Cloudrail will review the Load Balancers within your AWS account and Terraform plan to check if they are configured to drop invalid HTTP headers.