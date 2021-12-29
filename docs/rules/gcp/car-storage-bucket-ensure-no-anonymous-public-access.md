# Ensure that Cloud Storage bucket is not anonymously or publicly accessible

*Google Cloud Platform (GCP) > IAM*

![Cloudrail and Google Cloud Platform (GCP) logos](../images/cloudrail_gcp.png)

## Details
It is recommended that IAM policy on Cloud Storage bucket does not allow anonymous or public access as allowing such access can compromise private and sensitive data.

- **Severity**: 🔴 Major
- **Provider**: Google Cloud Platform (GCP)
- **Category**: IAM
- **Rule ID**: car_storage_bucket_ensure_no_anonymous_public_access

---

## Remediation
Information on how to fix "Ensure that Cloud Storage bucket is not anonymously or publicly accessible" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the resources google_storage_bucket_iam_member and google_storage_bucket_iam_binding ensure the attribute “members” doesn’t include allUsers and/or allAuthenticatedUsers.



##### Example Vulnerable Terraform Resource
The following is an example terraform resource vulnerable to *car_storage_bucket_ensure_no_anonymous_public_access*.
```hcl
resource "google_storage_default_object_access_control" "bucket_access_rule" {
  bucket = google_storage_bucket.bucket.name
  role   = "READER"
  entity = "allUsers"
}

resource "google_storage_bucket" "bucket" {
  name     = "example-bucket"
  location = "US"
}


```



##### Example Fixed Terraform Resource
The following is an example terraform resource that has been patched to address the rule.
```hcl
resource "google_storage_default_object_access_control" "bucket_access_rule" {
  bucket = google_storage_bucket.bucket.name
  role   = "READER"
  entity = "user-liz@example.com"
}

resource "google_storage_bucket" "bucket" {
  name     = "example-bucket"
  location = "US"
}


```







####  <img src="../_media/emojis/gcp.png" alt="gcp" width="20"/> Console
Follow the guides at <https://cloud.google.com/storage/docs/access-control/iam-reference> and <https://cloud.google.com/storage/docs/access-control/making-data-public> in order to ensure cloud storage bucket is not anonymously or publicly accessible.




---

## How It Works
Cloudrail will review the storage bucket resources configuration within your GCP subscription and Terraform plan to ensure that they are not anonymously or publicly accessible.