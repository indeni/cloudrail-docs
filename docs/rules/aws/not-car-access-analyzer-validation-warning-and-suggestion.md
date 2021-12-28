# Ensure IAM policies pass Access Analyzer policy validation without WARNING and SUGGESTION issues

*Amazon Web Services (AWS) > IAM*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will send all of your IAM policies to the AWS Access Analyzer for Policy Validation. Any issues found by Access Analyzer at the WARNING and SUGGESTION severities will be highlighted as issues by Cloudrail under this rule.

- **Severity**: 🟢 Low
- **Provider**: Amazon Web Services (AWS)
- **Category**: IAM
- **Rule ID**: not_car_access_analyzer_validation_warning_and_suggestion

---

## Remediation
Information on how to fix "Ensure IAM policies pass Access Analyzer policy validation without WARNING and SUGGESTION issues" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
Review the findings and correct them within the policy.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
not_car_access_analyzer_validation_remediation_steps_template



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Review the findings and correct them within the policy.




---

## How It Works
Cloudrail will send all of your IAM policies to the AWS Access Analyzer for Policy Validation. Any issues found by Access Analyzer at the WARNING and SUGGESTION severities will be highlighted as issues by Cloudrail under this rule.