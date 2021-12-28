# Ensure Elasticsearch Domains being created are set to be encrypted at rest

*Amazon Web Services (AWS) > Database*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Elasticsearch Domains should be encrypted whenever possible. Because it is easy to do upon resource creation, Cloudrail will flag a violation if a domain that is set to be created does not have encryption at rest turn on.

- **Severity**: 🔴 Major
- **Provider**: Amazon Web Services (AWS)
- **Category**: Database
- **Rule ID**: non_car_es_domain_encrypt_at_rest_creating

---

## Remediation
Information on how to fix "Ensure Elasticsearch Domains being created are set to be encrypted at rest" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_elasticsearch_domain resource, configure encrypt_at_rest block with argument enabled = true.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::Elasticsearch::Domain resource, configure EncryptionAtRestOptions block with Enabled argument set to true.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/encryption-at-rest.html> to enable encryption at rest for Elasticsearch domain.




---

## How It Works
Cloudrail will review the Elasticsearch domains being created in your environment. If a domain is not set to encrypt at rest, Cloudrail will highlight it as a violation. This rule will only flag a violation for resources that are not yet created.