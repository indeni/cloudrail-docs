# Ensure that VPC Flow Logs is enabled for every subnet in a VPC Network

*Google Cloud Platform (GCP) > Logging*

![Cloudrail and Google Cloud Platform (GCP) logos](../images/cloudrail_gcp.png)

## Details
Flow Logs provide visibility into network traffic for each VM inside the subnet and can be used to detect anomalous traffic or insight during security workflows. By default, the VPC Flow Logs feature is disabled when a new VPC network subnet is created. When enabled, VPC Flow Logs will start collecting network traffic data to and from your Virtual Private Cloud (VPC) subnets. Logging data can be useful for understanding network usage, network traffic expense optimization, network forensics, and real-time security analysis.

- **Severity**: 🟡 Medium
- **Provider**: Google Cloud Platform (GCP)
- **Category**: Logging
- **Rule ID**: non_car_compute_subnetwork_ensure_vpc_flow_logs_enabled

---

## Remediation
Information on how to fix "Ensure that VPC Flow Logs is enabled for every subnet in a VPC Network" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the google_compute_subnetwork resource ensure the log_config block exists with attributes.



##### Example Vulnerable Terraform Resource
The following is an example terraform resource vulnerable to *non_car_compute_subnetwork_ensure_vpc_flow_logs_enabled*.
```hcl
resource "google_compute_network" "example" {
  name                    = "example-network"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "example" {
  name          = "example-subnetwork"
  ip_cidr_range = "10.2.0.0/16"
  region        = "us-central1"
  network       = google_compute_network.example.id
  secondary_ip_range {
    range_name    = "tf-test-secondary-range-update1"
    ip_cidr_range = "192.168.10.0/24"
  }
}


```



##### Example Fixed Terraform Resource
The following is an example terraform resource that has been patched to address the rule.
```hcl
resource "google_compute_network" "example" {
  name                    = "example-network"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "example" {
  name          = "example-subnetwork"
  ip_cidr_range = "10.2.0.0/16"
  region        = "us-central1"
  network       = google_compute_network.example.id
  secondary_ip_range {
    range_name    = "tf-test-secondary-range-update1"
    ip_cidr_range = "192.168.10.0/24"
  }
  log_config {
    aggregation_interval = "INTERVAL_10_MIN"
    flow_sampling        = 0.5
    metadata             = "INCLUDE_ALL_METADATA"
  }
}

```







####  <img src="../_media/emojis/gcp.png" alt="gcp" width="20"/> Console
Follow the guides at <https://cloud.google.com/vpc/docs/using-flow-logs#enabling_vpc_flow_logging> in order to ensure VPC flow logging is enabled for every subnet in a VPC network.




---

## How It Works
Cloudrail will review the compute instances configuration within your GCP subscription and Terraform plan to ensure that flow logging is enabled for all the subnets in a VPC network.