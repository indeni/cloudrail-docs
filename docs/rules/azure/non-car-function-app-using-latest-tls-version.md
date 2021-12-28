# Ensure Function App is using the latest Azure supported TLS version (1.2)

*Microsoft Azure > Compute*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
Cloudrail will review the Function Apps configuration in your environment. If a function does not use the latest Azure supported TLS version (1.2), Cloudrail will highlight it as a violation.

- **Severity**: 🔴 Major
- **Provider**: Microsoft Azure
- **Category**: Compute
- **Rule ID**: non_car_function_app_using_latest_tls_version

---

## Remediation
Information on how to fix "Ensure Function App is using the latest Azure supported TLS version (1.2)" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the azurerm_function_app resource, in site_config block, set the min_tls_version argument to “1.2”.










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Follow the guide at <https://docs.microsoft.com/en-us/azure/app-service/configure-ssl-bindings#enforce-tls-versions> in order to set the Minimum TLS Version to 1.2 for the Function App.




---

## How It Works
Cloudrail will review the Function Apps configuration within your Azure subscription and Terraform plan to ensure they are using the latest Azure supported TLS version (1.2).