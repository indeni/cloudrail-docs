# Ensure no used security groups allow ingress from 0.0.0.0/0 or ::/0 to all ports

*Amazon Web Services (AWS) > Network*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Exposing resources to the Internet is generally inadvisable, especially to all ports range

- **Severity**: 🔴 Major
- **Provider**: Amazon Web Services (AWS)
- **Category**: Network
- **Rule ID**: public_access_security_groups_all_ports_rule

---

## Remediation
Information on how to fix "Ensure no used security groups allow ingress from 0.0.0.0/0 or ::/0 to all ports" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_security_group resource, modify in-line rules or the associated aws_security_group_rule resources to restrict traffic to specific ports. Additionally, for the aws_network_acl resource, modify in-line rules or the associated aws_network_acl_rule resources to restrict traffic to specific ports.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::EC2::SecurityGroup resource, modify in-line SecurityGroupIngress rules or the associated AWS::EC2::SecurityGroupIngress resources to restrict traffic to specific ports. Additionally, for the AWS::EC2::NetworkAcl resource, modify associated ingress AWS::EC2::NetworkAclEntry resources to restrict traffic to specific ports.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/working-with-security-groups.html#updating-security-group-rules> to update security groups rules and restrict traffic to specific ports. Additionally, follow the guide at <https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html#Rules> to update NACLs rules to restrict traffic to specific ports also.




---

## How It Works
Cloudrail will identify all security groups in use. For each one, it will determine if all ports range are exposed to `0.0.0.0/0`. Then, it will identify where the security group is in use. If it's not in use, the security group will be ignored. For each resource the security group is used with, Cloudrail will determine the subnet it is located in. It will then review the routing table to verify that the subnet is accessible from the Internet, and that the NACL associated with the subnet has all ports opened. This ensures the security group is only flagged if there's a real exposure.