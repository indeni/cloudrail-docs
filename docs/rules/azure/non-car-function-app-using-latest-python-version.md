# Ensure Function App is using the latest Python version

*Microsoft Azure > Compute*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
Cloudrail will review the Function Apps configuration in your environment. If a function of kind "functionapp" or "linux" is not using the latest Azure supported Python version (3.9), Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Microsoft Azure
- **Category**: Compute
- **Rule ID**: non_car_function_app_using_latest_python_version

---

## Remediation
Information on how to fix "Ensure Function App is using the latest Python version" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the azurerm_function_app resource, in site_config block, set the linux_fx_version argument to "PYTHON|3.9".










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Follow the guide at <https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python> in order to configure the latest Python version for the Function app.




---

## How It Works
Cloudrail will review the Function Apps configuration within your Azure subscription and Terraform plan to ensure that, if they are of kind "functionapp" or "linux", they are using the latest Azure supported Python version (3.9). You will need to check the resource azurerm_app_service_plan, associated to the Function app (app_service_plan_id), in order to get the "kind" argument.