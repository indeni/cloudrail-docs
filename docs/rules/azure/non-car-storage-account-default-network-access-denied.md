# Ensure Storage Account has default network access denied

*Microsoft Azure > Storage*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
Cloudrail will review the Storage Accounts configuration in your environment. If the account network rules are not denying default network access, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Microsoft Azure
- **Category**: Storage
- **Rule ID**: non_car_storage_account_default_network_access_denied

---

## Remediation
Information on how to fix "Ensure Storage Account has default network access denied" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the azurerm_storage_account resource, in the network_rules block, set the default_action argument to “Deny”. If azurerm_storage_account_network_rules resource is being used, set the default_action argument to “Deny”.










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Follow the guide at <https://docs.microsoft.com/en-us/azure/storage/common/storage-network-security?tabs=azure-portal#change-the-default-network-access-rule> in order to deny access by default.




---

## How It Works
Cloudrail will review the Storage Account configuration within your Azure subscription and Terraform plan to ensure that its network rules (either defined in-line or using azurerm_storage_account_network_rules resource) are denying default network access.