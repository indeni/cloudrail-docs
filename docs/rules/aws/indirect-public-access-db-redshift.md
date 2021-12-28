# Ensure Redshift database is not accessible indirectly via a publicly accessible resource

*Amazon Web Services (AWS) > Database*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Many organizations would like to protect their databases by multiple layers. For instance, they would want to avoid a situation where a publicly-accessible EC2 instance can directly access a database. The reason behind this is to avoid having “two hops” into the database from the Internet.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Database
- **Rule ID**: indirect_public_access_db_redshift

---

## Remediation
Information on how to fix "Ensure Redshift database is not accessible indirectly via a publicly accessible resource" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_redshift_cluster resource, set vpc_security_group_ids or cluster_security_groups arguments to use a Security Group that blocks traffic from publicly-accessible AWS resources.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::Redshift::Cluster resource, set VpcSecurityGroupIds or ClusterSecurityGroups arguments to use a Security Group that blocks traffic from publicly-accessible AWS resources.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/redshift/latest/mgmt/managing-security-groups-console.html> to modify Redshift Security Groups to block traffic from publicly-accessible AWS resources.




---

## How It Works
Cloudrail will review all of the Redshift databases configured in your environment. For each database, it will review the security groups in use (where VPC or not), the subnets in use, the public IP configured (on or off) and other aspects. It will then attempt to determine if the database can be accessed from any of the compute resources you have on a public subnet (EC2, ECS, etc.). This determination will take into account the security groups, subnet information, routing and other information, instead of relying solely on the existence of a public IP address. By doing this context-based analysis, Cloudrail ensures that only databases which can truly be accessed by a publicly-accessible compute resource are highlighted.