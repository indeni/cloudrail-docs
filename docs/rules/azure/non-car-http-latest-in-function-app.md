# Ensure HTTP version is the latest in Function Apps

*Microsoft Azure > Compute*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
Cloudrail will review the App Service (Function Apps) configuration in your environment. If an app does not use the latest HTTP version, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Microsoft Azure
- **Category**: Compute
- **Rule ID**: non_car_http_latest_in_function_app

---

## Remediation
Information on how to fix "Ensure HTTP version is the latest in Function Apps" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the azurerm_function_app resource, set the site_config block with http2_enabled argument set to true.










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Follow the guide at <https://azure.microsoft.com/en-us/blog/announcing-http-2-support-in-azure-app-service/> in order to configure HTTP version for the web app.




---

## How It Works
Cloudrail will review the Function Apps configuration within your Azure subscription and Cloudrail will review the App Service configuration within your Azure subscription and Terraform plan to check if latest http version is configured for web apps.