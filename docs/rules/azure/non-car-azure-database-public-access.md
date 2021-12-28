# Ensure Azure database server is not set to be public

*Microsoft Azure > Database*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
Cloudrail will review settings of all of the database servers configured in Azure through the "Azure Database for …" functionality. If a database server is set to be public, Cloudrail will highlight it as a violation.

- **Severity**: 🔴 Major
- **Provider**: Microsoft Azure
- **Category**: Database
- **Rule ID**: non_car_azure_database_public_access

---

## Remediation
Information on how to fix "Ensure Azure database server is not set to be public" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
In the database server resource (such as azurerm_postgresql_server, azurerm_mssql_server, etc.), set public_network_access_enabled to false.










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Follow the guides at <https://docs.microsoft.com/en-us/azure/azure-sql/database/connectivity-settings>, <https://docs.microsoft.com/en-us/azure/postgresql/howto-deny-public-network-access>, <https://docs.microsoft.com/en-us/azure/mysql/howto-deny-public-network-access>, <https://docs.microsoft.com/en-us/azure/mariadb/howto-deny-public-network-access>, in order to disable public network access for the database.




---

## How It Works
Cloudrail will review all of the Azure database servers declared in Terraform, and those already existing in the Azure environment, to determine if any of them is set to have public access enabled.