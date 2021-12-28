# Ensure SQL servers have auditing enabled

*Microsoft Azure > Database*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
Having ‘auditing’ enabled on SQL servers would help to track database activities. Cloudrail will review the MS SQL servers configuration in your environment and if a server does not have an auditing policy configured, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Microsoft Azure
- **Category**: Database
- **Rule ID**: non_car_sql_servers_auditing_enabled

---

## Remediation
Information on how to fix "Ensure SQL servers have auditing enabled" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the azurerm_mssql_server resource, add the extended_auditing_policy block and set the retention_in_days argument to 0 (unlimited) or a value greater than 90 and set the log_monitoring_enabled argument to true if you wish to send audit logs to Azure Monitor. If using the azurerm_mssql_server_extended_auditing_policy resource, create it with the same previous arguments.










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Follow the guide at <https://docs.microsoft.com/en-us/azure/azure-sql/database/auditing-overview> in order to configure auditing for SQL servers.




---

## How It Works
Cloudrail will review the SQL servers configuration within your Azure subscription and Terraform plan to ensure that auditing is enabled.