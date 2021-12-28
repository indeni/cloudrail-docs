# Ensure PostgreSQL database ‘log_temp_files’ flag is set to 0

*Google Cloud Platform (GCP) > Database*

![Cloudrail and Google Cloud Platform (GCP) logos](../images/cloudrail_gcp.png)

## Details
PostgreSQL can create a temporary file for actions such as sorting, hashing and temporary query results when these operations exceed work_mem. Configuring log_temp_files to 0 causes all temporary file information to be logged. If all temporary files are not logged, it may be difficult to identify potential performance issues that may be due to either poor application coding or deliberate resource starvation attempts.

- **Severity**: 🟡 Medium
- **Provider**: Google Cloud Platform (GCP)
- **Category**: Database
- **Rule ID**: non_car_cloud_sql_log_temp_files_zero

---

## Remediation
Information on how to fix "Ensure PostgreSQL database ‘log_temp_files’ flag is set to 0" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the google_sql_database_instance resources, ensure that log_temp_files database flag is set to 0 for PostgreSQL databases.










####  <img src="../_media/emojis/gcp.png" alt="gcp" width="20"/> Console
Follow the guide at <https://cloud.google.com/sql/docs/postgres/flags#setting_a_database_flag> in order to ensure that log_temp_files database flag is set to 0.




---

## How It Works
Cloudrail will review the database instance configuration within your GCP subscription and Terraform plan to ensure that PostgreSQL database instances have log_temp_files database flag set to 0.