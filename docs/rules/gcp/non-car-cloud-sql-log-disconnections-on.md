# Ensure PostgreSQL database ‘log_disconnections’ flag is set to ‘on’

*Google Cloud Platform (GCP) > Database*

![Cloudrail and Google Cloud Platform (GCP) logos](../images/cloudrail_gcp.png)

## Details
PostgreSQL does not log session details such as duration and session end by default. Enabling the log_disconnections setting will create log entries at the end of each session which can be useful in troubleshooting issues and determine any unusual activity across a time period. This recommendation is applicable to PostgreSQL database instances.

- **Severity**: 🟡 Medium
- **Provider**: Google Cloud Platform (GCP)
- **Category**: Database
- **Rule ID**: non_car_cloud_sql_log_disconnections_on

---

## Remediation
Information on how to fix "Ensure PostgreSQL database ‘log_disconnections’ flag is set to ‘on’" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the google_sql_database_instance resources, ensure that log_disconnections database flag is set to on for PostgreSQL databases.










####  <img src="../_media/emojis/gcp.png" alt="gcp" width="20"/> Console
Follow the guide at <https://cloud.google.com/sql/docs/postgres/flags#setting_a_database_flag> in order to ensure that log_disconnections database flag is set to on.




---

## How It Works
Cloudrail will review the database instance configuration within your GCP subscription and Terraform plan to ensure that PostgreSQL database instances have log_disconnections database flag set to on.