# Ensure Azure Defender for App Services is enabled

*Microsoft Azure > Security_Services*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
Cloudrail will review the Security Center subscription pricing configuration in your environment. If the tier is not set to “Standard” for App Services resources, Cloudrail will highlight it as a violation.

- **Severity**: 🔴 Major
- **Provider**: Microsoft Azure
- **Category**: Security_Services
- **Rule ID**: non_car_azure_defender_for_app_services_enabled

---

## Remediation
Information on how to fix "Ensure Azure Defender for App Services is enabled" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the azurerm_security_center_subscription_pricing resource, set the tier argument to “Standard” and ensure the resource_type argument contains the value “AppServices”.










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Follow the guide at <https://docs.microsoft.com/en-us/azure/security-center/enable-azure-defender> in order to enable Azure Defender for App Services.




---

## How It Works
Cloudrail will review the Security Center Subscription Pricing configuration within your Azure subscription and Terraform plan to ensure Azure Defender is enabled (“Standard” tier pricing) for App Services.