# Ensure PostgreSQL Servers are enforcing SSL

*Microsoft Azure > Database*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
Cloudrail will review the PostgreSQL servers configuration in your environment. If a server is not enforcing SSL connections, Cloudrail will highlight it as a violation.

- **Severity**: 🔴 Major
- **Provider**: Microsoft Azure
- **Category**: Database
- **Rule ID**: non_car_postgresql_server_enforcing_ssl

---

## Remediation
Information on how to fix "Ensure PostgreSQL Servers are enforcing SSL" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the azurerm_postgresql_server resource, set the ssl_enforcement_enabled argument to true.










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Follow the guide at <https://docs.microsoft.com/en-us/azure/postgresql/concepts-ssl-connection-security> in order to enable “Enforce SSL connection” for the PostgreSQL server.




---

## How It Works
Cloudrail will review the PostgreSQL Servers configuration within your Azure subscription and Terraform plan to ensure that SSL enforcement is enabled.