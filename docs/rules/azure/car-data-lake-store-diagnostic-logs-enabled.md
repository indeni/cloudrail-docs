# Ensure Data Lake Store has diagnostic logs enabled

*Microsoft Azure > Compute*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
Cloudrail will review the Data Lake Stores configuration in your environment. If data lake store does not have diagnostic logs enabled, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Microsoft Azure
- **Category**: Compute
- **Rule ID**: car_data_lake_store_diagnostic_logs_enabled

---

## Remediation
Information on how to fix "Ensure Data Lake Store has diagnostic logs enabled" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
Create an azurerm_monitor_diagnostic_setting resource and set the target_resource_id to the Data Lake Store ID. In the log block, set the enabled argument to true. In the log, retention_policy block, set enabled argument to true and days argument to 0 (indefinitely) or a value greater than or equal to 365.










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Follow the guide at <https://docs.microsoft.com/en-us/azure/data-lake-store/data-lake-store-diagnostic-logs#enable-diagnostic-logging-for-your-data-lake-storage-gen1-account> in order to enable diagnostic logs for the Data Lake Store.




---

## How It Works
Cloudrail will review the Data Lake Stores and Monitor diagnostic settings configuration within your Azure subscription and Terraform plan to ensure that Data Lake Stores have diagnostic logs enabled.