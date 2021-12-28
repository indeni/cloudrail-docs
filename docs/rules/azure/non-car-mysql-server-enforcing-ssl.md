# Ensure MySQL Servers are enforcing SSL

*Microsoft Azure > Database*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
Cloudrail will review the MySQL servers configuration in your environment. If a server is not enforcing SSL connections, Cloudrail will highlight it as a violation.

- **Severity**: 🔴 Major
- **Provider**: Microsoft Azure
- **Category**: Database
- **Rule ID**: non_car_mysql_server_enforcing_ssl

---

## Remediation
Information on how to fix "Ensure MySQL Servers are enforcing SSL" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the azurerm_mysql_server resource, set the ssl_enforcement_enabled argument to true.










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Follow the guide at <https://docs.microsoft.com/en-us/azure/mysql/howto-configure-ssl#step-3--enforcing-ssl-connections-in-azure> in order to enable “Enforce SSL connection” for the MySQL server.




---

## How It Works
Cloudrail will review the MySQL Servers configuration within your Azure subscription and Terraform plan to ensure that SSL enforcement is enabled.