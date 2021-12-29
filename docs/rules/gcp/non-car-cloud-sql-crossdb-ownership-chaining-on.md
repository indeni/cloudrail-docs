# Ensure SQL database ‘cross db ownership chaining’ flag is set to ‘on'

*Google Cloud Platform (GCP) > Database*

![Cloudrail and Google Cloud Platform (GCP) logos](../images/cloudrail_gcp.png)

## Details
The ‘cross db ownership chaining’ database flag allows the admins to control cross-database ownership chaining at the database level or to allow cross-database ownership chaining for all databases. Enabling cross db ownership is not recommended unless all of the databases hosted by the instance of SQL Server must participate in cross- database ownership chaining. This recommendation is applicable to SQL Server database instances.

- **Severity**: 🟡 Medium
- **Provider**: Google Cloud Platform (GCP)
- **Category**: Database
- **Rule ID**: non_car_cloud_sql_crossdb_ownership_chaining_on

---

## Remediation
Information on how to fix "Ensure SQL database ‘cross db ownership chaining’ flag is set to ‘on'" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the google_sql_database_instance resources, ensure that ‘cross db ownership chaining’ database flag is set to off for SQL Server databases.



##### Example Vulnerable Terraform Resource
The following is an example terraform resource vulnerable to *non_car_cloud_sql_crossdb_ownership_chaining_on*.
```hcl
resource "google_sql_database_instance" "master" {
  name             = "master-instance"
  database_version = "SQLSERVER_2017_STANDARD"
  region           = "us-central1"

}


```



##### Example Fixed Terraform Resource
The following is an example terraform resource that has been patched to address the rule.
```hcl
resource "google_sql_database_instance" "master" {
  name             = "master-instance"
  database_version = "SQLSERVER_2019_STANDARD"
  region           = "us-central1"
  
  settings {
    database_flags {
        name  = "cross db ownership chaining"
        value = "off"
    }
  }
}


```







####  <img src="../_media/emojis/gcp.png" alt="gcp" width="20"/> Console
Follow the guide at <https://cloud.google.com/sql/docs/sqlserver/flags> in order to ensure that ‘cross db ownership chaining’ database flag is set to off.



##### Example CLI Command
The following is an example CLI command used to address the rule violation.
```sh
DATABASE_INSTANCE_NAME=your_instance_name
gcloud sql instances patch $DATABASE_INSTANCE_NAME --database-flags "cross db ownership chaining=off"

```


---

## How It Works
Cloudrail will review the database instance configuration within your GCP subscription and Terraform plan to ensure that SQL Server database instances have ‘cross db ownership chaining’ database flag set to off.