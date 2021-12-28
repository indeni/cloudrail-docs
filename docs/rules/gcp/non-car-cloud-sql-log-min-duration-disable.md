# Ensure PostgreSQL database ‘log_min_duration_statement’ flag is set to -1

*Google Cloud Platform (GCP) > Database*

![Cloudrail and Google Cloud Platform (GCP) logos](../images/cloudrail_gcp.png)

## Details
The log_min_duration_statement flag defines the minimum amount of execution time of a statement in milliseconds where the total duration of the statement is logged. Ensure that log_min_duration_statement is disabled, i.e., a value of -1 is set. Logging SQL statements may include sensitive information that should not be recorded in logs. This recommendation is applicable to PostgreSQL database instances.

- **Severity**: 🟡 Medium
- **Provider**: Google Cloud Platform (GCP)
- **Category**: Database
- **Rule ID**: non_car_cloud_sql_log_min_duration_disable

---

## Remediation
Information on how to fix "Ensure PostgreSQL database ‘log_min_duration_statement’ flag is set to -1" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the google_sql_database_instance resources, ensure that log_min_duration_statement database flag is set to -1 for PostgreSQL databases.










####  <img src="../_media/emojis/gcp.png" alt="gcp" width="20"/> Console
Follow the guide at <https://cloud.google.com/sql/docs/postgres/flags#setting_a_database_flag> in order to ensure that log_min_duration_statement database flag is set to -1.




---

## How It Works
Cloudrail will review the database instance configuration within your GCP subscription and Terraform plan to ensure that PostgreSQL database instances have log_min_duration_statement database flag set to -1.