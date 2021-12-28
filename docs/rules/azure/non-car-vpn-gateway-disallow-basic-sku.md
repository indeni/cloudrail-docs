# Ensure Azure VPN gateways don't use the basic SKU

*Microsoft Azure > Network*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
The Azure VPN Gateway has different SKUs to choose from, each with different capabilities. The "basic" one is lacking many features and will generally not support anything beyond the smallest load.

- **Severity**: 🟡 Medium
- **Provider**: Microsoft Azure
- **Category**: Network
- **Rule ID**: non_car_vpn_gateway_disallow_basic_sku

---

## Remediation
Information on how to fix "Ensure Azure VPN gateways don't use the basic SKU" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
Change the 'sku' in the azurerm_virtual_network_gateway to a value that is not "Basic".










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Change the SKU of the VPN gateway by deleting the old one and creating a new one with a different SKU.




---

## How It Works
Cloudrail will review all of the VPN gateways in your Azure environment. If any uses the "basic" SKU, Cloudrail will raise a violation.