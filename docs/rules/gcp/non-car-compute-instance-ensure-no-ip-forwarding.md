# Ensure that IP forwarding is not enabled on Instances

*Google Cloud Platform (GCP) > Compute*

![Cloudrail and Google Cloud Platform (GCP) logos](../images/cloudrail_gcp.png)

## Details
Compute instances with ip forwarding enabled can perform the functions of routing or forwarding packets and hence it should be disabled to prevent data loss or information disclosure.  Instances created by GKE should be excluded because they need to have IP forwarding enabled and cannot be changed.

- **Severity**: 🟡 Medium
- **Provider**: Google Cloud Platform (GCP)
- **Category**: Compute
- **Rule ID**: non_car_compute_instance_ensure_no_ip_forwarding

---

## Remediation
Information on how to fix "Ensure that IP forwarding is not enabled on Instances" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the google_compute_instance resource ensure the attribute can_ip_forward is not set to true.










####  <img src="../_media/emojis/gcp.png" alt="gcp" width="20"/> Console
Follow the guides at <https://cloud.google.com/vpc/docs/using-routes#canipforward>  in order to disable ip forwarding feature of the compute VM instances.




---

## How It Works
Cloudrail will review the compute instances configuration within your GCP subscription and Terraform plan to ensure that ip forwarding is disabled.