# Ensure authentication is enabled in Function Apps

*Microsoft Azure > Compute*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
Cloudrail will review the Function Apps configuration in your environment. If a function does not have authentication enabled, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Microsoft Azure
- **Category**: Compute
- **Rule ID**: non_car_authentication_enabled_in_function_app

---

## Remediation
Information on how to fix "Ensure authentication is enabled in Function Apps" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the azurerm_function_app resource, set the auth_settings block with enabled argument set to true.










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Follow the guide at <https://docs.microsoft.com/en-us/azure/azure-functions/functions-how-to-use-azure-function-app-settings?tabs=portal#auth> in order to enable authentication for the Function App.




---

## How It Works
Cloudrail will review the Function Apps configuration within your Azure subscription and Terraform plan to check if authentication is enabled.