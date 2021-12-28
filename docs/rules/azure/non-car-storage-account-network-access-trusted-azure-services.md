# Ensure Storage Account is allowing network access to trusted Azure services

*Microsoft Azure > Storage*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
Cloudrail will review the Storage Accounts configuration in your environment. If the account network rules are not allowing access to trusted Azure services, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Microsoft Azure
- **Category**: Storage
- **Rule ID**: non_car_storage_account_network_access_trusted_azure_services

---

## Remediation
Information on how to fix "Ensure Storage Account is allowing network access to trusted Azure services" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the azurerm_storage_account resource, in the network_rules block, set the bypass argument to “AzureServices”. If azurerm_storage_account_network_rules resource is being used, set the bypass argument to “AzureServices”.










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Follow the guide at <https://docs.microsoft.com/en-us/azure/storage/common/storage-network-security?tabs=azure-portal#grant-access-to-trusted-azure-services> in order to grant access to trusted Azure services.




---

## How It Works
Cloudrail will review the Storage Account configuration within your Azure subscription and Terraform plan to ensure that trusted Azure services have network access to the account.