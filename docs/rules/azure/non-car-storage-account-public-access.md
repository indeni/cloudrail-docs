# Ensure Storage Account does not allow public access

*Microsoft Azure > Storage*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
Cloudrail will review the Storage Accounts configuration in your environment. If an account is allowing public access to containers and blobs, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Microsoft Azure
- **Category**: Storage
- **Rule ID**: non_car_storage_account_public_access

---

## Remediation
Information on how to fix "Ensure Storage Account does not allow public access" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the azurerm_storage_account resource, set the allow_blob_public_access argument to false.










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Follow the guide at <https://docs.microsoft.com/en-us/azure/storage/blobs/anonymous-read-access-configure?tabs=portal#allow-or-disallow-public-read-access-for-a-storage-account> in order to set Blob public access to Disabled.




---

## How It Works
Cloudrail will review the Storage Account configuration within your Azure subscription and Terraform plan to ensure that public access is disabled.