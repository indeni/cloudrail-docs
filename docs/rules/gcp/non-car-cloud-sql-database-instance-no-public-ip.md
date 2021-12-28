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










####  <img src="../_media/emojis/gcp.png" alt="gcp" width="20"/> Console
Follow the guides at <https://cloud.google.com/sql/docs/mysql/private-ip>  and <https://console.cloud.google.com/iam-admin/orgpolicies/sql-restrictPublicIp>  in order to ensure that private IPs are used instead of public IPs.




---

## How It Works
Cloudrail will review the database instance configuration within your GCP subscription and Terraform plan to ensure that Google Cloud database instances have 'ipv4_enabled' attribute not set to true.