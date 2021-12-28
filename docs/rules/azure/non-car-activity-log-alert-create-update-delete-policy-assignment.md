# Ensure that Activity Log Alert exists for Create/Update/Delete Policy Assignment events

*Microsoft Azure > IAM*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
Cloudrail will review the Activity Log Alerts configuration in your environment. If there are no alerts, or they are disabled, for Create/Update/Delete Policy Assignment events, Cloudrail will highlight it as a violation.

- **Severity**: 🔴 Major
- **Provider**: Microsoft Azure
- **Category**: IAM
- **Rule ID**: non_car_activity_log_alert_create_update_delete_policy_assignment

---

## Remediation
Information on how to fix "Ensure that Activity Log Alert exists for Create/Update/Delete Policy Assignment events" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the azurerm_monitor_activity_log_alert resource, set the scope argument to your subscription ID, set enabled argument to true. In the criteria block, set category argument to “Policy Assignment” and set the operation_name argument to one of these values "Microsoft.Authorization/policyAssignments/write", "Microsoft.Authorization/policyAssignments/delete". A resource azurerm_monitor_activity_log_alert must be created for each operation_name..










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Follow the guide at <https://docs.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-activity-log> in order to configure Alerts for Create/Update/Delete Policy Assignment events.




---

## How It Works
Cloudrail will review the Activity Log Alerts configuration within your Azure subscription and Terraform plan. to ensure that enabled Activity Log Alerts exist for Create/Update/Delete Policy Assignment events.