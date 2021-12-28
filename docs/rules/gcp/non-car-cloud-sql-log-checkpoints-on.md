# Ensure PostgreSQL database ‘log_checkpoints’ flag is set to ‘on’

*Google Cloud Platform (GCP) > Database*

![Cloudrail and Google Cloud Platform (GCP) logos](../images/cloudrail_gcp.png)

## Details
Enabling log_checkpoints causes checkpoints and restart points to be logged in the server log. Some statistics are included in the log messages, including the number of buffers written and the time spent writing them. This recommendation is applicable to PostgreSQL database instances.

- **Severity**: 🟡 Medium
- **Provider**: Google Cloud Platform (GCP)
- **Category**: Database
- **Rule ID**: non_car_cloud_sql_log_checkpoints_on

---

## Remediation
Information on how to fix "Ensure PostgreSQL database ‘log_checkpoints’ flag is set to ‘on’" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the google_sql_database_instance resources, ensure that log_checkpoints database flag is set to on for PostgreSQL databases.










####  <img src="../_media/emojis/gcp.png" alt="gcp" width="20"/> Console
Follow the guide at <https://cloud.google.com/sql/docs/postgres/flags#setting_a_database_flag> in order to ensure that log_checkpoints database flag is set to on.




---

## How It Works
Cloudrail will review the database instance configuration within your GCP subscription and Terraform plan to ensure that PostgreSQL database instances have log_checkpoints database flag set to on.