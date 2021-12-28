# Ensure Function App enforces FTPS only

*Microsoft Azure > Compute*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
Cloudrail will review the Function App configuration in your environment. If a function app has FTP enabled and it is not enforcing FTPS only, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Microsoft Azure
- **Category**: Compute
- **Rule ID**: non_car_function_app_enforces_ftps_only

---

## Remediation
Information on how to fix "Ensure Function App enforces FTPS only" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the azurerm_function_app resource, set the site_config block with ftps_state argument set to "FtpsOnly".










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Follow the guide at <https://docs.microsoft.com/en-us/azure/app-service/deploy-ftp?tabs=portal#enforce-ftps> in order to select FTPS Only in FTP state.




---

## How It Works
Cloudrail will review the Function Apps configuration within your Azure subscription and Terraform plan to check if they are enforcing FTPS only or if they have FTP disabled.