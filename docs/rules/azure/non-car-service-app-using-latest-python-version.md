# Ensure Web App is using the latest Azure supported Python version

*Microsoft Azure > Compute*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
Cloudrail will review the Web Apps configuration in your environment. If an app of kind "linux" does not use the latest Azure supported Python version, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Microsoft Azure
- **Category**: Compute
- **Rule ID**: non_car_service_app_using_latest_python_version

---

## Remediation
Information on how to fix "Ensure Web App is using the latest Azure supported Python version" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the azurerm_app_service resource, in site_config block, set the linux_fx_version argument to "PYTHON|3.9".










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Follow the guide at <https://docs.microsoft.com/en-us/azure/app-service/configure-language-python> in order to configure the latest Python version for the Web app.




---

## How It Works
Cloudrail will review the Web Apps configuration within your Azure subscription and Terraform plan to ensure that, if they are of kind "linux", they are using the latest Azure supported Python version. You will need to check the resource azurerm_app_service_plan, associated to the Web app (app_service_plan_id), in order to get the "kind" argument.