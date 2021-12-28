# Ensure no used security groups allow ingress from 0.0.0.0/0 or ::/0 to port 2483 (ORACLE DB)

*Amazon Web Services (AWS) > Compute*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Exposing resources to the Internet is generally inadvisable, especially on a known port like 2483 (ORACLE DB).

- **Severity**: 🔴 Major
- **Provider**: Amazon Web Services (AWS)
- **Category**: Compute
- **Rule ID**: public_access_security_groups_oracle_db_port_rule

---

## Remediation
Information on how to fix "Ensure no used security groups allow ingress from 0.0.0.0/0 or ::/0 to port 2483 (ORACLE DB)" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the resource aws_security_group, update in-line ingress rules or resource aws_security_group_rule to set cidr_blocks argument to a value other than `0.0.0.0/0` or `::/0` for the ORACLE DB port.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the resource AWS::EC2::SecurityGroup, update in-line SecurityGroupIngress or resource AWS::EC2::SecurityGroupIngress to set CidrIp argument to a value other than `0.0.0.0/0` or `::/0` for the ORACLE DB ToPort.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/working-with-security-groups.html#updating-security-group-rules> to update the security group inbound rule. Set the Source parameter to a value other than `0.0.0.0/0` or `::/0` for the ORACLE DB port.




---

## How It Works
Cloudrail will identify all security groups in use. For each one, it will determine if it has 2483 (ORACLE DB) exposed to `0.0.0.0/0`. Then, it will identify where the security group is in use. If it's not in use, the security group will be ignored. For each resource the security group is used with, Cloudrail will determine the subnet it is located in. It will then review the routing table to verify that the subnet is accessible from the Internet, and that the NACL associated with the subnet has the aforementioned port open. This ensures the security group is only flagged if there's a real exposure.