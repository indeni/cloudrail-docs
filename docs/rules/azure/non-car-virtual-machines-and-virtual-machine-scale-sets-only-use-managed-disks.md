# Ensure Virtual Machines and Virtual Machine Scale Sets only use managed disks

*Microsoft Azure > Compute*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
Cloudrail will review the Virtual Machines and Virtual Machine Scale Sets configuration in your environment. If they are using unmanaged disks, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Microsoft Azure
- **Category**: Compute
- **Rule ID**: non_car_virtual_machines_and_virtual_machine_scale_sets_only_use_managed_disks

---

## Remediation
Information on how to fix "Ensure Virtual Machines and Virtual Machine Scale Sets only use managed disks" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the azurerm_virtual_machine resource, in storage_os_disk block, remove vhd_uri or image_uri arguments and set managed_disk_type and managed_disk_id arguments or create an azurerm_virtual_machine_data_disk_attachment resource. For azurerm_virtual_machine_scale_set resource, in storage_profile_os_disk block, remove vhd_containers or image arguments and set managed_disk_type argument.










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Follow the guide at <https://docs.microsoft.com/en-us/azure/virtual-machines/managed-disks-overview> in order to attach managed disks to a Virtual Machine. Follow the guide at <https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/tutorial-use-disks-powershell> in order to attach managed disks to a Virtual Machine Scale Set.




---

## How It Works
Cloudrail will review the Virtual Machines and Virtual Machines Scale Sets configuration within your Azure subscription and Terraform plan to ensure they are using Managed Disks.