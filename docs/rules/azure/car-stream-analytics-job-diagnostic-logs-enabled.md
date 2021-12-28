# Ensure Stream Analytics job has diagnostic logs enabled

*Microsoft Azure > Streaming*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
Cloudrail will review the Stream Analytics jobs configuration in your environment. If a job does not have diagnostic logs enabled, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Microsoft Azure
- **Category**: Streaming
- **Rule ID**: car_stream_analytics_job_diagnostic_logs_enabled

---

## Remediation
Information on how to fix "Ensure Stream Analytics job has diagnostic logs enabled" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
Create an azurerm_monitor_diagnostic_setting resource and set the target_resource_id to the Stream Analytics job ID. In the log block, set the enabled argument to true. In the log, retention_policy block, set enabled argument to true and days argument to 0 (indefinitely) or a value greater than or equal to 365.










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Follow the guide at <https://docs.microsoft.com/en-us/azure/stream-analytics/stream-analytics-job-diagnostic-logs#send-diagnostics-to-azure-monitor-logs> in order to enable diagnostic logs for the Stream Analytics job.




---

## How It Works
Cloudrail will review the Stream Analytics jobs and Monitor diagnostic settings configuration within your Azure subscription and Terraform plan to ensure that Stream Analytics jobs have diagnostic logs enabled.