# Ensure diagnostic logs are enabled in App Services

*Microsoft Azure > Compute*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
Cloudrail will review the App Services configuration in your environment. If an app does not have diagnostic logs enabled (detailed error messages, HTTP logging, and failed requests tracing), Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Microsoft Azure
- **Category**: Compute
- **Rule ID**: non_car_diagnostic_logs_enabled_in_app_services

---

## Remediation
Information on how to fix "Ensure diagnostic logs are enabled in App Services" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the azurerm_app_service resource, set the log block with detailed_error_messages_enabled argument set to true, failed_request_tracing_enabled argument set to true, and http_logs block with either file_system or azure_blob_storage arguments set.










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Follow the guide at <https://docs.microsoft.com/en-us/azure/app-service/troubleshoot-diagnostic-logs> in order to enable diagnostics logging for apps in App Service.




---

## How It Works
Cloudrail will review the App Service configuration within your Azure subscription and Terraform plan to check if diagnostic logs are enabled.