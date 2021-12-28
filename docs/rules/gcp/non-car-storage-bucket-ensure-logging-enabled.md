# Ensure that logging is enabled for cloud storage buckets

*Google Cloud Platform (GCP) > Storage*

![Cloudrail and Google Cloud Platform (GCP) logos](../images/cloudrail_gcp.png)

## Details
It is recommended that storage access logs and storage logs are enabled for every storage bucket.

- **Severity**: 🟡 Medium
- **Provider**: Google Cloud Platform (GCP)
- **Category**: Storage
- **Rule ID**: non_car_storage_bucket_ensure_logging_enabled

---

## Remediation
Information on how to fix "Ensure that logging is enabled for cloud storage buckets" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the resource google_storage_bucket ensure that the optional attribute block “logging” is configured.










####  <img src="../_media/emojis/gcp.png" alt="gcp" width="20"/> Console
Follow the guides at <https://cloud.google.com/storage/docs/access-logs> in order to ensure cloud storage logs are enabled for every storage bucket.




---

## How It Works
Cloudrail will review the storage bucket resources configuration within your GCP subscription and Terraform plan to ensure that logging is enabled.