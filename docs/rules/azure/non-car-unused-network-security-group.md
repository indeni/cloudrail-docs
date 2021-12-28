# Ensure no unused Network Security Group exists in the subscription

*Microsoft Azure > Compute*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
Network Security Groups should be maintained carefully, in order to provide network access for desired entities. Having unused Network Security Groups is giving the opportunity to accidentally assign vulnerable network access to your resources.

- **Severity**: 🟡 Medium
- **Provider**: Microsoft Azure
- **Category**: Compute
- **Rule ID**: non_car_unused_network_security_group

---

## Remediation
Information on how to fix "Ensure no unused Network Security Group exists in the subscription" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
Remove the unused azurerm_network_security_group resource, from your TF template.










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Delete the unused Network Security Group from your Azure Portal.




---

## How It Works
Cloudrail will review all of the Network Security Groups defined in your subscription. For each Network Security Group which is present, but not attached to any network interfaces, Cloudrail will raise a violation.