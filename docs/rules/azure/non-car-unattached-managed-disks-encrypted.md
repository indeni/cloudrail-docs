# Ensure unattached Managed Disk are encrypted

*Microsoft Azure > Storage*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
Cloudrail will review the unattached Managed Disks configuration in your environment. If a disk is not encrypted, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Microsoft Azure
- **Category**: Storage
- **Rule ID**: non_car_unattached_managed_disks_encrypted

---

## Remediation
Information on how to fix "Ensure unattached Managed Disk are encrypted" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the azurerm_managed_disk resource, set the encryption_settings block with enabled argument set to true, or create an azurerm_disk_encryption_set resource and set the disk_encryption_set_id argument.










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Follow the guide at <https://docs.microsoft.com/en-us/azure/virtual-machines/disk-encryption> to enable disk encryption.




---

## How It Works
Cloudrail will review the unattached Managed Disks configuration within your Azure subscription and Terraform plan to ensure they are encrypted. To find unattached disks on the TF plan, the azurerm_virtual_machine_data_disk_attachment resources should be scanned.