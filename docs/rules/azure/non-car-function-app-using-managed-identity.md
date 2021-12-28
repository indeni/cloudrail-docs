# Ensure Function App is using a managed identity

*Microsoft Azure > Compute*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
Cloudrail will review the Function Apps configuration in your environment. If a function of type “functionapp” does not have a managed identity enabled, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Microsoft Azure
- **Category**: Compute
- **Rule ID**: non_car_function_app_using_managed_identity

---

## Remediation
Information on how to fix "Ensure Function App is using a managed identity" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the azure_function_app resource, in identity block, set the type argument to “SystemAssigned”, or to “UserAssigned” and also set identity_ids argument.










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Follow the guide at <https://docs.microsoft.com/en-us/azure/app-service/overview-managed-identity?toc=%2Fazure%2Fazure-functions%2Ftoc.json&tabs=dotnet> in order to configure a managed identity for the Function app.




---

## How It Works
Cloudrail will review the Function Apps configuration within your Azure subscription and Terraform plan to ensure that, if they are of kind “functionapp”, they are using the managed identities. You will need to check the resource azurerm_app_service_plan, associated to the Function app (app_service_plan_id), in order to get the “kind” argument.