# Ensure DocDB clusters are set to encrypt the connection with applications

*Amazon Web Services (AWS) > Database*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the DocDB clusters in your environment. If a cluster is not set to encrypt in transit, Cloudrail will highlight it as a violation. This rule will only flag a violation for resources that are not yet created.

- **Severity**: 🔴 Major
- **Provider**: Amazon Web Services (AWS)
- **Category**: Database
- **Rule ID**: not_car_docdb_cluster_encrypted_in_transit

---

## Remediation
Information on how to fix "Ensure DocDB clusters are set to encrypt the connection with applications" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_docdb_cluster_parameter_group resource, in parameter block, ensure parameter "name" is equal to "tls" and "value" is equal to "enabled", or just remove those two parameter to create the DocDB cluster with encryption in transit enabled by default.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::DocDB::DBClusterParameterGroup resource, ensure Parameters argument contains the 'tls' key with value 'enabled', or just remove them to create the DocDB cluster with encryption in transit enabled by default.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/documentdb/latest/developerguide/security.encryption.ssl.html> to enable encryption in transit.




---

## How It Works
Cloudrail will identify all DocumentDB clusters within your AWS account and Terraform plan that are not configured to perform encryption in transit.