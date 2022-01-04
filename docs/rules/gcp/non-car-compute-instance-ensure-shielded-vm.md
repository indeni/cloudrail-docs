# Ensure Compute instances are launched with Shielded VM enabled

*Google Cloud Platform (GCP) > Compute*

![Cloudrail and Google Cloud Platform (GCP) logos](../images/cloudrail_gcp.png)

## Details
Shielded VMs are virtual machines (VMs) hardened by a set of security controls that help defend against rootkits and bootkits. Shielded VM instances run firmware which is signed and verified using Google's Certificate Authority, ensuring that the instance's firmware is unmodified and establishing the root of trust for secure boot. Shielded VM's verifiable integrity is achieved through the use of secure boot, virtual trusted platform module (vTPM), and integrity monitoring.

- **Severity**: 🟡 Medium
- **Provider**: Google Cloud Platform (GCP)
- **Category**: Compute
- **Rule ID**: non_car_compute_instance_ensure_shielded_vm

---

## Remediation
Information on how to fix "Ensure Compute instances are launched with Shielded VM enabled" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the google_compute_instance resource ensure the shielded_instance_config block has attributes enable_secure_boot, enable_vtpm and enable_integrity_monitoring set to true.



##### Example Vulnerable Terraform Resource
The following is an example terraform resource vulnerable to *non_car_compute_instance_ensure_shielded_vm*.
```hcl
resource "google_compute_instance" "shielded_vm_test" {
  name         = "shielded-vm-test"
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



##### Example Fixed Terraform Resource
The following is an example terraform resource that has been patched to address the rule.
```hcl
resource "google_compute_instance" "shielded_vm_test" {
  name         = "shielded-vm-test"
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

  shielded_instance_config {
    enable_secure_boot = true
  }

}

```







####  <img src="../_media/emojis/gcp.png" alt="gcp" width="20"/> Console
Follow the guides at <https://cloud.google.com/compute/docs/instances/modifying-shielded-vm> in order to turn on vTPM and integrity monitoring of VM instances.




---

## How It Works
Cloudrail will review the compute instances configuration within your GCP subscription and Terraform plan to ensure that the instances have Shielded VM attributes enabled.