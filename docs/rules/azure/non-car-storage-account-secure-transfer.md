# Ensure Storage Account requires secure transfer

*Microsoft Azure > Storage*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
Cloudrail will review the Storage Accounts configuration in your environment. If an account is not requiring secure transfer (HTTPS), Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Microsoft Azure
- **Category**: Storage
- **Rule ID**: non_car_storage_account_secure_transfer

---

## Remediation
Information on how to fix "Ensure Storage Account requires secure transfer" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the azurerm_storage_account resource, set the enable_https_traffic_only argument to true.










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Follow the guide at <https://docs.microsoft.com/en-us/azure/storage/common/storage-require-secure-transfer> in order to enable secure transfer.




---

## How It Works
Cloudrail will review the Storage Account configuration within your Azure subscription and Terraform plan to ensure that secure transfer is enabled.