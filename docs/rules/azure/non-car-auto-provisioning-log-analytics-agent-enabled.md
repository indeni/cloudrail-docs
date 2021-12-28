# Ensure Auto provisioning of the Log Analytics agent is enabled on your subscription

*Microsoft Azure > Security_Services*

![Cloudrail and Microsoft Azure logos](../images/cloudrail_azure.png)

## Details
Cloudrail will review the Security Center Auto Provisioning configuration in your environment. If the auto provision of the Log Analytics agent is not set to On, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Microsoft Azure
- **Category**: Security_Services
- **Rule ID**: non_car_auto_provisioning_log_analytics_agent_enabled

---

## Remediation
Information on how to fix "Ensure Auto provisioning of the Log Analytics agent is enabled on your subscription" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the azurerm_security_center_auto_provisioning resource, set the auto_provision argument to “On”.










####  <img src="../_media/emojis/azure.png" alt="azure" width="20"/> Console
Follow the guide at <https://docs.microsoft.com/en-us/azure/security-center/security-center-enable-data-collection#enable-auto-provisioning-of-the-log-analytics-agent-and-extensions-> in order to enable the automatic provision of the Log Analytics agent.




---

## How It Works
Cloudrail will review the Function Apps configuration within your Azure subscription and Terraform plan to check if authentication is enabled.