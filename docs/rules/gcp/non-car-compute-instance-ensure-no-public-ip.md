# Ensure that Compute instances do not have public IP addresses

*Google Cloud Platform (GCP) > Compute*

![Cloudrail and Google Cloud Platform (GCP) logos](../images/cloudrail_gcp.png)

## Details
To reduce your attack surface, it is highly recommended that compute instances should not have public IP addresses. Instead, instances should be configured behind load balancers, to minimize the instance's exposure to the internet. Instances created by GKE should be excluded because some of them have external IP addresses and cannot be changed by editing the instance settings.

- **Severity**: 🔴 Major
- **Provider**: Google Cloud Platform (GCP)
- **Category**: Compute
- **Rule ID**: non_car_compute_instance_ensure_no_public_ip

---

## Remediation
Information on how to fix "Ensure that Compute instances do not have public IP addresses" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the google_compute_instance resource ensure the access_config sub block under network_interface is removed.



##### Example Vulnerable Terraform Resource
The following is an example terraform resource vulnerable to *non_car_compute_instance_ensure_no_public_ip*.
```hcl
resource "google_compute_address" "static" {
  name = "ipv4-address"
}

resource "google_compute_instance" "no_public_ip_test" {
  name         = "no-public-ip-test"
  machine_type = "e2-medium"
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-9"
    }
  }

  network_interface {
    network = "default"
    access_config {
      nat_ip = google_compute_address.static.address
    }
  }
}


```



##### Example Fixed Terraform Resource
The following is an example terraform resource that has been patched to address the rule.
```hcl
resource "google_compute_instance" "no_public_ip_test" {
  name         = "no-public-ip-test"
  machine_type = "e2-medium"
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-9"
    }
  }

  network_interface {
    network = "default"
  }
}

```







####  <img src="../_media/emojis/gcp.png" alt="gcp" width="20"/> Console
Follow the guides at <https://cloud.google.com/compute/docs/ip-addresses/reserve-static-external-ip-address#disableexternalip> in order to disable external IP address of the compute VM instances.




---

## How It Works
Cloudrail will review the compute instances configuration within your GCP subscription and Terraform plan to ensure that they do not have external IP address.