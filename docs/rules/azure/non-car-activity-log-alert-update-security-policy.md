# Ensure that Activity Log Alert exists for Create/Update/Delete Security Policy events

*Microsoft Azure > Security_Services*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
Cloudrail will review the Activity Log Alerts configuration in your environment. If there are no alerts, or they are disabled, for Create/Update/Delete Security Policy events, Cloudrail will highlight it as a violation.

- **Severity**: 🔴 Major
- **Provider**: Microsoft Azure
- **Category**: Security_Services
- **Rule ID**: non_car_activity_log_alert_update_security_policy

---

## Remediation
Information on how to fix "Ensure that Activity Log Alert exists for Create/Update/Delete Security Policy events" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the azurerm_monitor_activity_log_alert resource, set the scope argument to your subscription ID, set enabled argument to true. In the criteria block, set category argument to “Security Policy” and set the operation_name argument to Microsoft.Security/policies/write..










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Follow the guide at <https://docs.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-activity-log> in order to configure Alerts for Create/Update/Delete Security Policy events.




---

## How It Works
Cloudrail will review the Activity Log Alerts configuration within your Azure subscription and Terraform plan. to ensure that enabled Activity Log Alerts exist for Create/Update/Delete Security Policy events.