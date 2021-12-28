# Ensure PostgreSQL database ‘log_min_error_statement’ flag is set to a valid value

*Google Cloud Platform (GCP) > Database*

![Cloudrail and Google Cloud Platform (GCP) logos](../images/cloudrail_gcp.png)

## Details
If log_min_error_statement is not set to the correct value, messages may not be classified as error messages appropriately. The log_min_error_statement flag should be set in accordance with the organization's logging policy. This recommendation is applicable to PostgreSQL database instances.

- **Severity**: 🟡 Medium
- **Provider**: Google Cloud Platform (GCP)
- **Category**: Database
- **Rule ID**: non_car_cloud_sql_log_min_error

---

## Remediation
Information on how to fix "Ensure PostgreSQL database ‘log_min_error_statement’ flag is set to a valid value" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the google_sql_database_instance resources, ensure that log_lock_waits database flag is set to on for PostgreSQL databases.










####  <img src="../_media/emojis/gcp.png" alt="gcp" width="20"/> Console
Follow the guide at <https://cloud.google.com/sql/docs/postgres/flags#setting_a_database_flag> in order to ensure that log_min_error_statement database flag is set to value in [DEBUG5, DEBUG4, DEBUG3, DEBUG2, DEBUG1, INFO, NOTICE, WARNING, ERROR, LOG, FATAL, or PANIC].




---

## How It Works
Cloudrail will review the database instance configuration within your GCP subscription and Terraform plan to ensure that PostgreSQL database instances have log_min_error_statement database flag set to a valid value.