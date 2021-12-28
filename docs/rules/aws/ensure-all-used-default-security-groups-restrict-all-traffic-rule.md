# Ensure all used default security groups of every VPC restrict all traffic

*Amazon Web Services (AWS) > Network*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Using default security groups in general is inadvisable. By locking security groups down, you are validating that if anyone uses them by accident, they will realize before any security issues occur.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Network
- **Rule ID**: ensure_all_used_default_security_groups_restrict_all_traffic_rule

---

## Remediation
Information on how to fix "Ensure all used default security groups of every VPC restrict all traffic" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the resource aws_default_security_group, update the inline ingress and egress rules.










####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/working-with-security-groups.html#deleting-security-group-rule> to update the security group rules.




---

## How It Works
Cloudrail will review all of the default security groups configured in your environment. It will then cross reference these security groups with the resources they are used with, to determine they are used at all. For each of those default security groups that are used, Cloudrail will determine if they allow any ingress or egress traffic. By doing this context-based analysis, Cloudrail ensures that only default security groups who pose a true security risk are highlighted.