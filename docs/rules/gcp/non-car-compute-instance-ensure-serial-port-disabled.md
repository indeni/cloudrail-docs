# Ensure ‘Enable connecting to serial ports’ is not enabled for VM Instance

*Google Cloud Platform (GCP) > Compute*

![Cloudrail and Google Cloud Platform (GCP) logos](../images/cloudrail_gcp.png)

## Details
The interactive serial console does not support IP-based access restrictions such as IP whitelists. If the interactive serial console is enabled on an instance, clients can attempt to connect to that instance from any IP address. This allows unwanted access to that instance if they know the correct SSH key, username, project ID, zone, and instance name. Hence interactive serial console support should be disabled.

- **Severity**: 🔴 Major
- **Provider**: Google Cloud Platform (GCP)
- **Category**: Compute
- **Rule ID**: non_car_compute_instance_ensure_serial_port_disabled

---

## Remediation
Information on how to fix "Ensure ‘Enable connecting to serial ports’ is not enabled for VM Instance" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the google_compute_instance resource ensure the metadata serial-port-enable is not set to true (default is false).










####  <img src="../_media/emojis/gcp.png" alt="gcp" width="20"/> Console
Follow the guides at <https://cloud.google.com/compute/docs/instances/interacting-with-serial-console> in order to disable the serial console access to the compute VM instance.




---

## How It Works
Cloudrail will review the compute instances configuration within your GCP subscription and Terraform plan to ensure that metadata value for serial-port-enable is not set to true.