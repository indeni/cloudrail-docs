# Ensure Elasticsearch Domain is not accessible indirectly via a publicly accessible resource

*Amazon Web Services (AWS) > Database*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Many organizations would like to protect their Elasticsearch domains by multiple layers. For instance, they would want to avoid a situation where a publicly-accessible EC2 instance can directly access an ES domain. The reason behind this is to avoid having “two hops” into the ES domain from the Internet.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Database
- **Rule ID**: indirect_public_access_elastic_search_rule

---

## Remediation
Information on how to fix "Ensure Elasticsearch Domain is not accessible indirectly via a publicly accessible resource" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_elasticsearch_domain resource, in vpc_options block, set security_group_ids argument to reference a Security Group that blocks access from compute resources in public subnets.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::Elasticsearch::Domain resource, in VPCOptions block, set SecurityGroupIds argument to reference a Security Group that blocks access from compute resources in public subnets.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html> to configure the Security Groups to block access from compute resources in public subnets.




---

## How It Works
Cloudrail will review all of the ES domains configured in your environment. For each database, it will review the security groups in use (whether VPC or not), the subnets in use, the public IP configured (on or off) and other aspects. It will then attempt to determine if the ES domain can be accessed from any of the compute resources you have on a public subnet (EC2, ECS, etc.). This determination will take into account the security groups, subnet information, routing and other information, instead of relying solely on the existence of a public IP address. By doing this context-based analysis, Cloudrail ensures that only domains which can truly be accessed by a publicly-accessible compute resource are highlighted.