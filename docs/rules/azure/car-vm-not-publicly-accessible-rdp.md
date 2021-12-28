# Ensure VM is not publicly accessible via RDP

*Microsoft Azure > Network*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
Having Virtual Machines accessible publicly from the Internet on known administrative or management ports can be problematic. Cloudraill will attempt to determine if any of the virtual machines are accessible directly at their public IP address, or indirectly via NAT, at RDP’s port. If they are, a violation will be raised.

- **Severity**: 🔴 Major
- **Provider**: Microsoft Azure
- **Category**: Network
- **Rule ID**: car_vm_not_publicly_accessible_rdp

---

## Remediation
Information on how to fix "Ensure VM is not publicly accessible via RDP" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
Follow the guide at <https://docs.microsoft.com/en-us/azure/virtual-network/manage-network-security-group> in order to modify the Network Security Group rule to restrict RDP access from the Internet by setting a specific source IP address.










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Follow the guide at <https://docs.microsoft.com/en-us/azure/virtual-network/manage-network-security-group> in order to modify the Network Security Group rule to restrict RDP access from the Internet by setting a specific source IP address.




---

## How It Works
Cloudrail will review the Virtual Machines configuration within your Azure subscription and Terraform plan. For each virtual machine, it will check the attached network interfaces that are reachable from the Internet, either using a public IP or an inbound NAT rule. It will ensure that the Network Security Groups of the NIC and the subnet are not allowing inbound TCP access to destination port RDPz (3389, “*”, or a port range containing 3389) for any source IP address prefix (“*”, “Internet”).