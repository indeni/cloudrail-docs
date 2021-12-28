# Ensure authentication is enabled in Web Apps

*Microsoft Azure > Compute*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
Cloudrail will review the App Service (Web Apps) configuration in your environment. If an app does not have authentication enabled, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Microsoft Azure
- **Category**: Compute
- **Rule ID**: non_car_authentication_enabled_in_web_app

---

## Remediation
Information on how to fix "Ensure authentication is enabled in Web Apps" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the azurerm_app_service resource, set the auth_settings block with enabled argument set to true.










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Follow the guide at <https://docs.microsoft.com/en-us/azure/app-service/overview-authentication-authorization> in order to enable authentication for the web app.




---

## How It Works
Cloudrail will review the App Service configuration within your Azure subscription and Terraform plan to check if authentication is enabled for web apps.