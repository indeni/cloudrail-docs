# Ensure Storage Account allows network access using virtual network rules

*Microsoft Azure > Storage*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
Cloudrail will review the Storage Accounts configuration in your environment. If an account is using IP rules instead of virtual network rules for network access, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Microsoft Azure
- **Category**: Storage
- **Rule ID**: non_car_storage_account_network_access_virtual_network_rules

---

## Remediation
Information on how to fix "Ensure Storage Account allows network access using virtual network rules" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the azurerm_storage_account resource, in the network_rules block, delete the ip_rules argument and set the virtual_network_subnet_ids argument to the list of subnet IDs allowed to access the storage account. If azurerm_storage_account_network_rules resource is being used, delete the ip_rules argument and set the virtual_network_subnet_ids argument to the list of subnet IDs allowed to access the storage account.










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Follow the guide at <https://docs.microsoft.com/en-us/azure/storage/common/storage-network-security?tabs=azure-portal#grant-access-from-a-virtual-network> in order to set network access based on virtual network rules.




---

## How It Works
Cloudrail will review the Storage Accounts configuration within your Azure subscription and Terraform plan to check if network rules are based on IP rules (list of public IPs) instead of virtual network rules.