# Ensure that all Cloud SQL database instances have backup configuration enabled

*Google Cloud Platform (GCP) > Database*

![Cloudrail and Google Cloud Platform (GCP) logos](../images/cloudrail_gcp.png)

## Details
Backups provide a way to restore a Cloud SQL instance to recover lost data or recover from a problem with that instance. Automated backups need to be set for any instance that contains data that should be protected from loss or damage.

- **Severity**: 🟡 Medium
- **Provider**: Google Cloud Platform (GCP)
- **Category**: Database
- **Rule ID**: non_car_cloud_sql_enable_backup

---

## Remediation
Information on how to fix "Ensure that all Cloud SQL database instances have backup configuration enabled" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the google_sql_database_instance resources, ensure that backup_configuration option is set to enabled with start_time configured in 24 hr format in UTC.



##### Example Vulnerable Terraform Resource
The following is an example terraform resource vulnerable to *non_car_cloud_sql_enable_backup*.
```hcl
resource "google_sql_database_instance" "backup-config-test" {
  name             = "backup-config-test"
  database_version = "POSTGRES_11"
  region           = "us-central1"

  settings {
    tier = "db-f1-micro"
  }
}


```



##### Example Fixed Terraform Resource
The following is an example terraform resource that has been patched to address the rule.
```hcl
resource "google_sql_database_instance" "backup-config-test" {
  name             = "backup-config-test"
  database_version = "POSTGRES_11"
  region           = "us-central1"

  settings {
    tier = "db-f1-micro"
  }
}

```







####  <img src="../_media/emojis/gcp.png" alt="gcp" width="20"/> Console
Follow the guide at <https://cloud.google.com/sql/docs/mysql/create-instance#>  in order to ensure that automated backups are set to enabled and backup time is mentioned.




---

## How It Works
Cloudrail will review the database instance configuration within your GCP subscription and Terraform plan to ensure that database connections has backup_configured set to enabled with a specified start time.