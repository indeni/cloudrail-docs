# Ensure SQL database requires SSL

*Google Cloud Platform (GCP) > Database*

![Cloudrail and Google Cloud Platform (GCP) logos](../images/cloudrail_gcp.png)

## Details
Ensure SQL database requires SSL

- **Severity**: 🔴 Major
- **Provider**: Google Cloud Platform (GCP)
- **Category**: Database
- **Rule ID**: non_car_gcp_sql_database_ssl_required

---

## Remediation
Information on how to fix "Ensure SQL database requires SSL" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
Ensure SQL database requires SSL



##### Example Vulnerable Terraform Resource
The following is an example terraform resource vulnerable to *non_car_gcp_sql_database_ssl_required*.
```hcl
resource "google_sql_database_instance" "example" {
  name             = "example-instance"
  database_version = "MYSQL_5_7"
  settings {
    tier = "db-f1-micro"
  }
}


```



##### Example Fixed Terraform Resource
The following is an example terraform resource that has been patched to address the rule.
```hcl
resource "google_sql_database_instance" "example" {
  name             = "example-instance"
  database_version = "MYSQL_5_7"
  settings {
    tier = "db-f1-micro"
    ip_configuration {
        require_ssl = true
    }
  }
}

```







####  <img src="../_media/emojis/gcp.png" alt="gcp" width="20"/> Console
Ensure SQL database requires SSL



##### Example CLI Command
The following is an example CLI command used to address the rule violation.
```sh
INSTANCE_NAME=your_cloudsql_instance_name
gcloud sql instances patch $INSTANCE_NAME --require-ssl

```


---

## How It Works
Ensure SQL database requires SSL