# Ensure Data Lake Analytics account has diagnostic logs enabled

*Microsoft Azure > Database*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
Cloudrail will review the Data Lake Analytics account configuration in your environment. If an account does not have diagnostic logs enabled, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Microsoft Azure
- **Category**: Database
- **Rule ID**: car_data_lake_analytics_account_diagnostic_logs_enabled

---

## Remediation
Information on how to fix "Ensure Data Lake Analytics account has diagnostic logs enabled" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
Create an azurerm_monitor_diagnostic_setting resource and set the target_resource_id to the Data Lake Analytics account ID. In the log block, set the enabled argument to true. In the log, retention_policy block, set enabled argument to true and days argument to 0 (indefinitely) or a value greater than or equal to 365.










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Follow the guide at <https://docs.microsoft.com/en-us/azure/key-vault/general/alert> in order to enable diagnostic logs for the Data Lake Analytics account.




---

## How It Works
Cloudrail will review the Data Lake Analytics account and Monitor diagnostic settings configuration within your Azure subscription and Terraform plan to ensure that Data Lake Analytics account have diagnostic logs enabled.