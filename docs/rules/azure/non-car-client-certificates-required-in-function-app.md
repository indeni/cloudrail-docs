# Ensure client certificates are required in Function App

*Microsoft Azure > Compute*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
Cloudrail will review the Function Apps configuration in your environment. If a function does not have client certificates mode set to Required, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Microsoft Azure
- **Category**: Compute
- **Rule ID**: non_car_client_certificates_required_in_function_app

---

## Remediation
Information on how to fix "Ensure client certificates are required in Function App" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the azurerm_function_app resource, set the client_cert_mode argument to "Required".










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Follow the guide at https://docs.microsoft.com/en-us/azure/app-service/app-service-web-configure-tls-mutual-auth in order to require client certificates for Function App.




---

## How It Works
Cloudrail will review the Function Apps configuration within your Azure subscription and Terraform plan to ensure client certificates are required.