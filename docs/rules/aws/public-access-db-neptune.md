# Ensure Neptune database is not publicly accessible

*Amazon Web Services (AWS) > Database*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Databases should not be publicly accessible. If a database is serving content to be consumed by external users, it's best to go through an API gateway or some other control point.

- **Severity**: 🔴 Major
- **Provider**: Amazon Web Services (AWS)
- **Category**: Database
- **Rule ID**: public_access_db_neptune

---

## Remediation
Information on how to fix "Ensure Neptune database is not publicly accessible" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_neptune_cluster resource, set vpc_security_group_ids or cluster_security_groups arguments to use a Security Group that blocks traffic from publicly-accessible AWS resources.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::Neptune::DBCluster resource, set VpcSecurityGroupIds argument to use a Security Group that blocks traffic from publicly-accessible AWS resources.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/neptune/latest/userguide/security-vpc-security-group.html> to modify Neptune database Security Groups to block traffic from publicly-accessible AWS resources.




---

## How It Works
Cloudrail will review all of the Neptune databases configured in your environment. For each database, it will review the security groups in use (where VPC or not), the subnets in use, the public IP configured (on or off) and other aspects. It will then attempt to determine if the database can be accessed from the Internet. This determination will take into account the security groups, subnet information, routing and other information, instead of relying solely on the existence of a public IP address. By doing this context-based analysis, Cloudrail ensures that only databases which can truly be accessed from the Internet are highlighted.