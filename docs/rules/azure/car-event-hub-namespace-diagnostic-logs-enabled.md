# Ensure Event Hub namespace has diagnostic logs enabled

*Microsoft Azure > Streaming*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
Cloudrail will review the Event Hub namespace configuration in your environment. If namespace does not have diagnostic logs enabled, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Microsoft Azure
- **Category**: Streaming
- **Rule ID**: car_event_hub_namespace_diagnostic_logs_enabled

---

## Remediation
Information on how to fix "Ensure Event Hub namespace has diagnostic logs enabled" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
Create an azurerm_monitor_diagnostic_setting resource and set the target_resource_id to the Event Hub namespace ID. In the log block, set the enabled argument to true. In the log, retention_policy block, set enabled argument to true and days argument to 0 (indefinitely) or a value greater than or equal to 365.










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Follow the guide at <https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-diagnostic-logs> in order to enable diagnostic logs for the Event Hub namespace.




---

## How It Works
Cloudrail will review the Event Hub namespaces and Monitor diagnostic settings configuration within your Azure subscription and Terraform plan to ensure that Event Hub namespaces have diagnostic logs enabled.