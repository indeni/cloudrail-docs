# Ensure that Cloud SQL database instances do not have public IPs

*Google Cloud Platform (GCP) > Database*

![Cloudrail and Google Cloud Platform (GCP) logos](../images/cloudrail_gcp.png)

## Details
It is recommended to configure second generation sql instances to use private IPs and not public IPs to reduce the organization's attack surface.

- **Severity**: 🟡 Medium
- **Provider**: Google Cloud Platform (GCP)
- **Category**: Database
- **Rule ID**: non_car_cloud_sql_database_instance_no_public_ip

---

## Remediation
Information on how to fix "Ensure that Cloud SQL database instances do not have public IPs" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the google_sql_database_instance resources, ensure that ‘ipv4_enabled’ attribute is set to false for Google Cloud SQL database instances.



##### Example Vulnerable Terraform Resource
The following is an example terraform resource vulnerable to *non_car_cloud_sql_database_instance_no_public_ip*.
```hcl
resource "google_sql_database_instance" "instance" {
  name             = "example-instance"
  region           = "us-central1"
  database_version = "MYSQL_5_7"

  settings {
    tier = "db-f1-micro"
  }
}


```



##### Example Fixed Terraform Resource
The following is an example terraform resource that has been patched to address the rule.
```hcl
resource "google_sql_database_instance" "instance" {
  name             = "example-instance"
  region           = "us-central1"
  database_version = "MYSQL_5_7"

  depends_on = [google_service_networking_connection.private_vpc_connection]

  settings {
    tier = "db-f1-micro"
    ip_configuration {
      ipv4_enabled    = false
      private_network = google_compute_network.private_network.id
    }
  }
}

# A private network must also be configured to disable ipv4
resource "google_compute_network" "private_network" {
  name = "private-network"
}

resource "google_compute_global_address" "private_ip_address" {
  name          = "private-ip-address"
  purpose       = "VPC_PEERING"
  address_type  = "INTERNAL"
  prefix_length = 16
  network       = google_compute_network.private_network.id
}

resource "google_service_networking_connection" "private_vpc_connection" {
  network                 = google_compute_network.private_network.id
  service                 = "servicenetworking.googleapis.com"
  reserved_peering_ranges = [google_compute_global_address.private_ip_address.name]
}

```







####  <img src="../_media/emojis/gcp.png" alt="gcp" width="20"/> Console
Follow the guides at <https://cloud.google.com/sql/docs/mysql/private-ip>  and <https://console.cloud.google.com/iam-admin/orgpolicies/sql-restrictPublicIp>  in order to ensure that private IPs are used instead of public IPs.



##### Example CLI Command
The following is an example CLI command used to address the rule violation.
```sh
# This will result in instance downtime

# First configure the instance to use a private IP
INSTANCE_ID=your_instance_id
PROJECT_ID=your_gcp_project_id
VPC_NETWORK_NAME=your_vpc_network_name

gcloud beta sql instances patch $INSTANCE_ID \
--project=$PROJECT_ID \
--network=projects/$PROJECT_ID/global/networks/$VPC_NETWORK_NAME \
--no-assign-ip

# Then disable the instance ipv4
gcloud sql instances patch $INSTANCE_ID \
--no-assign-ip

# and confirm it's disabled
gcloud sql instances describe $INSTANCE_ID

```


---

## How It Works
Cloudrail will review the database instance configuration within your GCP subscription and Terraform plan to ensure that Google Cloud database instances have 'ipv4_enabled' attribute not set to true.