# Ensure Elasticsearch domains being created are set to be encrypted node-to-node

*Amazon Web Services (AWS) > Database*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the Elasticsearch domains being created in your environment. If a domain is not set to encrypt node-to-node communication, Cloudrail will highlight it as a violation. This rule will only flag a violation for resources that are not yet created.

- **Severity**: 🔴 Major
- **Provider**: Amazon Web Services (AWS)
- **Category**: Database
- **Rule ID**: not_car_elasticsearch_domains_encrypted_note_to_node

---

## Remediation
Information on how to fix "Ensure Elasticsearch domains being created are set to be encrypted node-to-node" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_elasticsearch_domain resource, configure node_to_node_encryption block with argument enabled = true.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::Elasticsearch::Domain resource, configure NodeToNodeEncryptionOptions block with Enabled argument set to true.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/ntn.html> to enable node-to-node encryption for Elasticsearch domain.




---

## How It Works
Cloudrail will identify all Elasticsearch domains in the Terraform plan that are going to be created and are not configured to encrypt node-to-node communication.