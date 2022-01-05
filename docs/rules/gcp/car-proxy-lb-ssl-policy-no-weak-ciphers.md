# Ensure no HTTPS or SSL proxy load balancers permit SSL policies with weak cipher suites

*Google Cloud Platform (GCP) > Network*

![Cloudrail and Google Cloud Platform (GCP) logos](../images/cloudrail_gcp.png)

## Details
Secure Sockets Layer (SSL) policies determine which Transport Layer Security (TLS) features clients are permitted to use when connecting to external Google Cloud load balancers. Using outdated and insecure ciphers for the SSL policies associated with your HTTPS/SSL Proxy load balancers could make the SSL connection between clients and load balancers vulnerable to exploits.

- **Severity**: 🔴 Major
- **Provider**: Google Cloud Platform (GCP)
- **Category**: Network
- **Rule ID**: car_proxy_lb_ssl_policy_no_weak_ciphers

---

## Remediation
Information on how to fix "Ensure no HTTPS or SSL proxy load balancers permit SSL policies with weak cipher suites" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the google_compute_ssl_policy resource, set the min_tls_version attribute to TLS_1_2 and profile attribute to MODERN or RESTRICTED or CUSTOM with ciphers not in [TLS_RSA_WITH_AES_128_GCM_SHA256, TLS_RSA_WITH_AES_256_GCM_SHA384, TLS_RSA_WITH_AES_128_CBC_SHA, TLS_RSA_WITH_AES_256_CBC_SHA, TLS_RSA_WITH_3DES_EDE_CBC_SHA].



##### Example Vulnerable Terraform Resource
The following is an example terraform resource vulnerable to *car_proxy_lb_ssl_policy_no_weak_ciphers*.
```hcl
resource "google_compute_ssl_policy" "example_ssl" {
  name            = "example-ssl-policy"
  min_tls_version = "TLS_1_0"
  profile         = "COMPATIBLE"
}


```



##### Example Fixed Terraform Resource
The following is an example terraform resource that has been patched to address the rule.
```hcl
resource "google_compute_ssl_policy" "example_ssl" {
  name            = "example-ssl-policy"
  min_tls_version = "TLS_1_2"
  profile         = "CUSTOM"
  custom_features = ["TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384", "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384"]
}

```







####  <img src="../_media/emojis/gcp.png" alt="gcp" width="20"/> Console
Follow the guide at <https://cloud.google.com/load-balancing/docs/use-ssl-policies> in order to modify ssl polices to use a minimum of TLS version 1.2 and set policy to modern or restricted or custom with ciphers not in [TLS_RSA_WITH_AES_128_GCM_SHA256, TLS_RSA_WITH_AES_256_GCM_SHA384, TLS_RSA_WITH_AES_128_CBC_SHA, TLS_RSA_WITH_AES_256_CBC_SHA, TLS_RSA_WITH_3DES_EDE_CBC_SHA].




---

## How It Works
Cloudrail will review the load balancer forwarding rules and target https/ssl proxy configuration within your GCP subscription and Terraform plan. For each forwarding rule and proxy, it will check the associated SSL Policy to ensure that the min TLS version is 1.2 and the profile is set to modern or restricted or custom with ciphers not in [TLS_RSA_WITH_AES_128_GCM_SHA256 or TLS_RSA_WITH_AES_256_GCM_SHA384 or TLS_RSA_WITH_AES_128_CBC_SHA or TLS_RSA_WITH_AES_256_CBC_SHA or TLS_RSA_WITH_3DES_EDE_CBC_SHA].