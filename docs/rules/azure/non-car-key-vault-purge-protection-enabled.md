# Ensure Key Vaults have purge protection enabled

*Microsoft Azure > Security_Services*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
Cloudrail will review the Key Vaults configuration in your environment. If a vault does not have purge protection enabled, Cloudrail will highlight it as a violation. Cloudrail does not access the contents of the vaults themselves.

- **Severity**: 🟡 Medium
- **Provider**: Microsoft Azure
- **Category**: Security_Services
- **Rule ID**: non_car_key_vault_purge_protection_enabled

---

## Remediation
Information on how to fix "Ensure Key Vaults have purge protection enabled" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the azurerm_key_vault resource, set the purge_protection_enabled argument to true.










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Follow the guide at <https://docs.microsoft.com/en-us/azure/key-vault/general/soft-delete-overview> in order to enable purge protection for a vault.




---

## How It Works
Cloudrail will review the Key Vault configuration within your Azure subscription and Terraform plan to ensure purge protection is enabled.