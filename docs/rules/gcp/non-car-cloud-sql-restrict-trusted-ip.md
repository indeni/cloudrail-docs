# Ensure that Cloud SQL database instances are not open to the world

*Google Cloud Platform (GCP) > Database*

![Cloudrail and Google Cloud Platform (GCP) logos](../images/cloudrail_gcp.png)

## Details
To minimize attack surface on a Database server instance, only trusted/known and required IP(s) should be allowedto connect to it. An authorized network should not have IPs/networks configured to `0.0.0.0/0` which will allow access to the instance from anywhere in the world. Note that authorized networks apply only to instances with public IPs.

- **Severity**: 🔴 Major
- **Provider**: Google Cloud Platform (GCP)
- **Category**: Database
- **Rule ID**: non_car_cloud_sql_restrict_trusted_ip

---

## Remediation
Information on how to fix "Ensure that Cloud SQL database instances are not open to the world" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the google_sql_database_instance resource, set the authorized Networks parameter under ipConfiguration subblock to value other than `0.0.0.0/0`.



##### Example Vulnerable Terraform Resource
The following is an example terraform resource vulnerable to *non_car_cloud_sql_restrict_trusted_ip*.
```hcl
resource "google_sql_database_instance" "example" {
  name             = "example-instance"
  database_version = "MYSQL_5_7"
  settings {
    tier = "db-f1-micro"
    ip_configuration {
        authorized_networks {
            name = "open-to-all"
            value = "0.0.0.0/0"
        }
    }
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
        authorized_networks {
            name = "open-to-specific-ip"
            value = "10.0.0.1/32"
        }
    }
  }
}

# ✅ 2021-12-29
```







####  <img src="../_media/emojis/gcp.png" alt="gcp" width="20"/> Console
Follow the guide at <https://console.cloud.google.com/sql/instances> in order to audit and delete any authorized networks with `0.0.0.0/0`.




---

## How It Works
Cloudrail will review the database instance configuration within your GCP subscription and Terraform plan to ensure that database connections are not permitted from `0.0.0.0/0`.