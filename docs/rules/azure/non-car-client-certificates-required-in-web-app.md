# Ensure client certificates are required in Web App

*Microsoft Azure > Compute*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
Cloudrail will review the Web Apps configuration in your environment. If an app does not have client certificates enabled, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Microsoft Azure
- **Category**: Compute
- **Rule ID**: non_car_client_certificates_required_in_web_app

---

## Remediation
Information on how to fix "Ensure client certificates are required in Web App" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the azurerm_app_service resource, set the client_cert_enabled argument to true.










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Follow the guide at <https://docs.microsoft.com/en-us/azure/app-service/app-service-web-configure-tls-mutual-auth> in order to enable client certificates for Web App.




---

## How It Works
Cloudrail will review the Web Apps configuration within your Azure subscription and Terraform plan to ensure client certificates are enabled.