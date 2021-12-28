# Ensure all resources that can be tagged have at least one tag

*Amazon Web Services (AWS) > All*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Some organizations require that all resources have at least one tag set. This rule will review the resources that can be tagged, and make sure each one has a tag that is not the Name tag. Resources that are not tagged will be flagged.

- **Severity**: 🟢 Low
- **Provider**: Amazon Web Services (AWS)
- **Category**: All
- **Rule ID**: non_car_all_resources_tagged

---

## Remediation
Information on how to fix "Ensure all resources that can be tagged have at least one tag" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
Add a tags section to the resource with at least one tag beyond the Name tag.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
Add a Tags section to the resource with at least one tag beyond the Name tag.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Access the specific resource in the AWS console and add tags.




---

## How It Works
Cloudrail will iterate over all resources in the cloud account and Terraform code, and for those that support tags, will check to see if they have any tags set other than the Name tag.