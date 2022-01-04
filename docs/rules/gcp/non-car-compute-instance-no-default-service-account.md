# Ensure that instances are not configured to use the default service account

*Google Cloud Platform (GCP) > Compute*

![Cloudrail and Google Cloud Platform (GCP) logos](../images/cloudrail_gcp.png)

## Details
The default compute engine service account has the Editor role on the project, which allows read and write access to most Google Cloud Services. To defend against privilege escalations if your VM is compromised and prevent an attacker from gaining access to all of your project, it is recommended to not use the default compute engine service account.

- **Severity**: 🟡 Medium
- **Provider**: Google Cloud Platform (GCP)
- **Category**: Compute
- **Rule ID**: non_car_compute_instance_no_default_service_account

---

## Remediation
Information on how to fix "Ensure that instances are not configured to use the default service account" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the google_compute_instance resource ensure the service_account block has attribute email doesn’t use default service account [project_number]- compute@developer.gserviceaccount.com.



##### Example Vulnerable Terraform Resource
The following is an example terraform resource vulnerable to *non_car_compute_instance_no_default_service_account*.
```hcl
resource "google_compute_instance" "default_service_account_test" {
  name         = "default-service-account-test"
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
resource "google_service_account" "new_service_account" {
  account_id   = "new_service_account"
  display_name = "New Service Account"
}

resource "google_compute_instance" "default_service_account_test" {
  name         = "default-service-account-test"
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

  service_account {
    email  = google_service_account.new_service_account.email
    scopes = ["cloud-platform"]
  }

}

```







####  <img src="../_media/emojis/gcp.png" alt="gcp" width="20"/> Console
Follow the guides at <https://cloud.google.com/compute/docs/access/service-accounts>  and <https://cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances> in order to ensure default service account is not used. VMs created by GKE should be excluded.




---

## How It Works
Cloudrail will review the compute instances configuration within your GCP subscription and Terraform plan to ensure that the instances do not use default service account.