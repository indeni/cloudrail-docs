# Ensure Elasticsearch Domain is not publicly accessible

*Amazon Web Services (AWS) > Database*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review all of the Elasticsearch domains configured in your environment. For each domain it will review if it is set to be publicly accessible.

- **Severity**: 🔴 Major
- **Provider**: Amazon Web Services (AWS)
- **Category**: Database
- **Rule ID**: public_access_elasticsearch_rule

---

## Remediation
Information on how to fix "Ensure Elasticsearch Domain is not publicly accessible" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_elasticsearch_domain resource, in vpc_options block, set subnet_ids and security_group_ids arguments.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::Elasticsearch::Domain resource, in VPCOptions block, set SubnetIds and SecurityGroupIds arguments.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html> to configure VPC access instead of Public access in Network configuration section.




---

## How It Works
Cloudrail will review all of the Elasticsearch domains configured in your environment. For each domain it will review if it is set to be publicly accessible.