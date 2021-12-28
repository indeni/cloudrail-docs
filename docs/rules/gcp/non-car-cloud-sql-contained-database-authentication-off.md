# Ensure SQL database ‘contained database authentication’ flag is set to ‘off’

*Google Cloud Platform (GCP) > Database*

![Cloudrail and Google Cloud Platform (GCP) logos](../images/cloudrail_gcp.png)

## Details
Contained databases have some unique threats that should be understood and mitigated by SQL Server Database Engine administrators. Most of the threats are related to the USER WITH PASSWORD authentication process, which moves the authentication boundary from the Database Engine level to the database level, hence it is recommended to disable ‘contained database authentication’ flag. This recommendation is applicable to SQL Server database instances. 

- **Severity**: 🟡 Medium
- **Provider**: Google Cloud Platform (GCP)
- **Category**: Database
- **Rule ID**: non_car_cloud_sql_contained_database_authentication_off

---

## Remediation
Information on how to fix "Ensure SQL database ‘contained database authentication’ flag is set to ‘off’" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the google_sql_database_instance resources, ensure that ‘contained database authentication’ database flag is set to off for SQL Server databases.










####  <img src="../_media/emojis/gcp.png" alt="gcp" width="20"/> Console
Follow the guide at <https://cloud.google.com/sql/docs/sqlserver/flags>  in order to ensure that ‘contained database authentication’ database flag is set to off.




---

## How It Works
Cloudrail will review the database instance configuration within your GCP subscription and Terraform plan to ensure that SQL Server database instances have ‘contained database authentication’ database flag set to off.