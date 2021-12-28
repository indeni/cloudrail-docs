# Ensure GKE Control Plane is not public

*Google Cloud Platform (GCP) > Kubernetes*

![Cloudrail and Google Cloud Platform (GCP) logos](../images/cloudrail_gcp.png)

## Details
Enable master authorized networks to restrict access to the GKE cluster's control plane to only an allow list of authorized IPs. Restricting access to an authorized network provides additional security benefits for the container cluster, such as better protection from outsider and insider attacks.

- **Severity**: 🔴 Major
- **Provider**: Google Cloud Platform (GCP)
- **Category**: Kubernetes
- **Rule ID**: non_car_gke_control_plane_ensure_not_public

---

## Remediation
Information on how to fix "Ensure GKE Control Plane is not public" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the resource google_container_cluster ensure the attribute block master_authorized_networks_config is configured with cidr ip address blocks.










####  <img src="../_media/emojis/gcp.png" alt="gcp" width="20"/> Console
Follow the guides at <https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks> in order to ensure GKE control plane is not publicly




---

## How It Works
Cloudrail will review the GKE container cluster resources configuration within your GCP subscription and Terraform plan to ensure that the control plane is not publicly accessible.