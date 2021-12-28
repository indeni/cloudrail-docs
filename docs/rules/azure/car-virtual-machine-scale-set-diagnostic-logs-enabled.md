# Ensure Virtual Machine Scale Set has diagnostic logs enabled

*Microsoft Azure > Compute*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
Cloudrail will review the Virtual Machine Scale Sets configuration in your environment. If a Scale Set does not have a diagnostic extension associated, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Microsoft Azure
- **Category**: Compute
- **Rule ID**: car_virtual_machine_scale_set_diagnostic_logs_enabled

---

## Remediation
Information on how to fix "Ensure Virtual Machine Scale Set has diagnostic logs enabled" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For azurerm_virtual_machine_scale_set resource, create an extension block with publisher and type arguments set. For azurerm_windows_virtual_machine_scale_set and azurerm_linux_virtual_machine_scale_set resources, create an azurerm_virtual_machine_scale_set_extension resource with publisher and type arguments set. The value for publisher argument should be "Microsoft.Azure.Diagnostics" (for Windows VMs) or "Microsoft.Azure.Diagnostics" or “"Microsoft.OSTCExtensions" (for Linux VMs). The value for type argument should be "LinuxDiagnostics" (for Linux VMs) or “IaaSDiagnostics” (for Windows VMs).










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Follow the guide at <https://docs.microsoft.com/en-us/azure/azure-monitor/agents/diagnostics-extension-overview> in order to configure the diagnostics extension for the Virtual Machine Scale Set.




---

## How It Works
Cloudrail will review the Virtual Machine Scale Sets configuration within your Azure subscription and Terraform plan to ensure that Diagnostics extension is enabled. For TF azurerm_virtual_machine_scale_set resource, an extension block (with the desired configuration) should exist. For TF azurerm_windows_virtual_machine_scale_set and azurerm_linux_virtual_machine_scale_set resources, an azurerm_virtual_machine_scale_set_extension resource should exit with the desired configuration.