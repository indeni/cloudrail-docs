# Ensure that instances are not configured to use the default service account with full access to all Cloud APIs

*Google Cloud Platform (GCP) > Compute*

![Cloudrail and Google Cloud Platform (GCP) logos](../images/cloudrail_gcp.png)

## Details
To ensure the principle of least privileges are followed and to prevent potential privilege escalation, the Compute Engine instances should not be configured to use the default service account with the Cloud API access scope set to "Allow full access to all Cloud APIs".

- **Severity**: 🟡 Medium
- **Provider**: Google Cloud Platform (GCP)
- **Category**: Compute
- **Rule ID**: non_car_compute_instance_no_default_service_account_full_access_api

---

## Remediation
Information on how to fix "Ensure that instances are not configured to use the default service account with full access to all Cloud APIs" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the google_compute_instance resource ensure the service_account block has attribute email doesn’t use default service account [project_number]- compute@developer.gserviceaccount.com and the scope is not set to https://www.googleapis.com/auth/cloud-platform.










####  <img src="../_media/emojis/gcp.png" alt="gcp" width="20"/> Console
Follow the guides at <https://cloud.google.com/compute/docs/access/service-accounts> and <https://cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances> in order to ensure default service account with scope Allow full access to all Cloud APIs is not being used. VMs created by GKE should be excluded.




---

## How It Works
Cloudrail will review the compute instances configuration within your GCP subscription and Terraform plan to ensure that the instances do not use default service account with scope Allow full access to all Cloud APIs.