# Ensure Function App is only accessible via HTTPS

*Microsoft Azure > Compute*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
Cloudrail will review the Function Apps configuration in your environment. If a function does not have HTTPS only enabled, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Microsoft Azure
- **Category**: Compute
- **Rule ID**: non_car_function_app_accessible_only_via_https

---

## Remediation
Information on how to fix "Ensure Function App is only accessible via HTTPS" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the azurerm_function_app resource, set the https_only argument to true.










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Follow the guide at <https://docs.microsoft.com/en-us/azure/app-service/configure-ssl-bindings#enforce-https> in order to configured HTTPS Only for the Function App.




---

## How It Works
Cloudrail will review the Function Apps configuration within your Azure subscription and Terraform plan to check if HTTPS only is enabled.