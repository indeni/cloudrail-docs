# Cloudrail Rules - {{ pretty_provider }}
Cloudrail rules for {{ pretty_provider }}, click on a rule for more details and how to fix it.

| Severity | Category | Name |
| ----------- | ----------- | ----------- |
{% for rule in rules %} | {{ rule['severity_emoji']}} | {{ rule['resource_types'] }} | [{{ rule['name'] }}](rules/{{ provider }}/{{ rule['slug'] }}) |
{% endfor %}
