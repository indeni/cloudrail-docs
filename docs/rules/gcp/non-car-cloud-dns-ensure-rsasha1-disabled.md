# Ensure that RSASHA1 is not used for the zone-signing and key-signing keys in Cloud DNS DNSSEC

*Google Cloud Platform (GCP) > Network*

![Cloudrail and Google Cloud Platform (GCP) logos](../images/cloudrail_gcp.png)

## Details
The algorithm used for key signing should be a recommended one and it should be strong. When enabling DNSSEC for a managed zone, or creating a managed zone with DNSSEC, the DNSSEC signing algorithms and the denial-of-existence type can be selected.

- **Severity**: 🟡 Medium
- **Provider**: Google Cloud Platform (GCP)
- **Category**: Network
- **Rule ID**: non_car_cloud_dns_ensure_rsasha1_disabled

---

## Remediation
Information on how to fix "Ensure that RSASHA1 is not used for the zone-signing and key-signing keys in Cloud DNS DNSSEC" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the google_dns_managed_zone resource ensure that dnssec_config block has "state" set to on and default_key_specs block has "algorithm" not set to rsasha1.










####  <img src="../_media/emojis/gcp.png" alt="gcp" width="20"/> Console
Follow the guide at <https://cloud.google.com/dns/dnssec-advanced#advanced_signing_options> in order to ensure rsasha1 is not used for zone-signing and key-signing keys.




---

## How It Works
Cloudrail will review the google dns zone configuration within your GCP subscription and Terraform plan to ensure that dnssec state is configured and rsasha1 is not used.