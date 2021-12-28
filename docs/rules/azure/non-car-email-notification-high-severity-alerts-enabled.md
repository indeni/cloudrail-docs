# Ensure Email notification for high severity alerts is enabled

*Microsoft Azure > Security_Services*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
Cloudrail will review the Security Center configuration in your environment. If email notification of high severity alerts is not enabled, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Microsoft Azure
- **Category**: Security_Services
- **Rule ID**: non_car_email_notification_high_severity_alerts_enabled

---

## Remediation
Information on how to fix "Ensure Email notification for high severity alerts is enabled" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the azurerm_security_center_contact resource, set the alert_notifications argument to true.










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Follow the guide at <https://docs.microsoft.com/en-us/azure/security-center/security-center-provide-security-contact-details> in order to enable email notifications for security alerts.




---

## How It Works
Cloudrail will review the Security Center Contact configuration within your Azure subscription and Terraform plan to ensure email notifications of security alerts is enabled.