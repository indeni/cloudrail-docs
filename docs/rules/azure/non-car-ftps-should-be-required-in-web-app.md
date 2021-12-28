# FTPS should be required in your Web App

*Microsoft Azure > Compute*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
Cloudrail will review the App service configuration in your environment. If an app has FTP enabled and is not enforcing FTPS only, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Microsoft Azure
- **Category**: Compute
- **Rule ID**: non_car_ftps_should_be_required_in_web_app

---

## Remediation
Information on how to fix "FTPS should be required in your Web App" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the azurerm_app_service resource, set the site_config block with ftps_state argument set to “FtpsOnly” to enforce FTPS or to “Disabled” if you want to disable FTP.










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Follow the guide at <https://docs.microsoft.com/en-us/azure/app-service/deploy-ftp?tabs=portal#enforce-ftps> in order to disable FTP or select FTPS Only in FTP state.




---

## How It Works
Cloudrail will review the App services configuration within your Azure subscription and Terraform plan to check if they are enforcing FTPS only or if they have FTP disabled.