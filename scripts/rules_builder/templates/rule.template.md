# {{ rule.name }}

*{{ rule.provider_pretty }} > {{ rule.resource_types }}*

![Cloudrail and {{ rule.provider_pretty }} logos]({{ rule.provider_image_url }})

## Details
{{ rule.description }}

- **Severity**: {{ rule.severity_emoji }} {{ rule.severity }}
- **Provider**: {{ rule.provider_pretty }}
- **Category**: {{ rule.resource_types }}
- **Rule ID**: {{ rule.id }}

---

## Remediation
Information on how to fix "{{ rule.name }}" using available methods.

{% if rule.remediation['terraform'] %}
####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
{{ rule.remediation['terraform']['text'] }}

{% if rule.remediation['terraform']['code_vulnerable'] %}

##### Example Vulnerable Terraform Resource
The following is an example terraform resource vulnerable to *{{ rule.id }}*.
```hcl
{{ rule.remediation['terraform']['code_vulnerable'] }}

```
{% endif %}

{% if rule.remediation['terraform']['code_fixed'] %}
##### Example Fixed Terraform Resource
The following is an example terraform resource that has been patched to address the rule.
```hcl
{{ rule.remediation['terraform']['code_fixed'] }}
```
{% endif %}

{% endif %}

{% if rule.remediation['cloudformation'] %}
#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
{{ rule.remediation['cloudformation']['text'] }}
{% endif %}

{% if rule.remediation['console'] %}
####  <img src="../_media/emojis/{{rule.provider}}.png" alt="{{rule.provider}}" width="20"/> Console
{{ rule.remediation['console']['text'] }}
{% endif %}

{% if rule.remediation['console']['code'] %}
##### Example CLI Command
The following is an example CLI command used to address the rule violation.
```sh
{{ rule.remediation['console']['code'] }}
```
{% endif %}

---

## How It Works
{{ rule.human_readable_logic }}
