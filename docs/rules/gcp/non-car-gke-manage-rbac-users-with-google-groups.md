# Manage Kubernetes RBAC users with Google Groups for GKE

*Google Cloud Platform (GCP) > Kubernetes*

![Cloudrail and Google Cloud Platform (GCP) logos](../images/cloudrail_gcp.png)

## Details
Cluster administrators should leverage G suite groups and cloud iam to assign kubernetes user roles to a collection of users, instead of to individual emails using only cloud iam. This prevents users gaining unique permissions sets that increase the cost of audit.

- **Severity**: 🟡 Medium
- **Provider**: Google Cloud Platform (GCP)
- **Category**: Kubernetes
- **Rule ID**: non_car_gke_manage_rbac_users_with_google_groups

---

## Remediation
Information on how to fix "Manage Kubernetes RBAC users with Google Groups for GKE" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the resource google_container_cluster ensure the attribute block authenticator_groups_config is configured with the right security groups.










####  <img src="../_media/emojis/gcp.png" alt="gcp" width="20"/> Console
Follow the guides at <https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control#google-groups-for-gke> in order to manage Kubernetes RBAC users with google groups.




---

## How It Works
Cloudrail will review the GKE container cluster resources configuration within your GCP subscription and Terraform plan to ensure that RBAC security group is being used for authentication.