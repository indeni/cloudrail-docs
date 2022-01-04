import pytest
from template_generator import TemplateGenerator
from cloudrail_formatted_rule import CloudrailFormattedRule


tg = TemplateGenerator()
provider = "gcp"
fp = f'knowledge/cloudrail/knowledge/rules/{provider}/{provider}_rules_metadata.yaml'
tg.templates[provider] = tg._get_yaml_file(fp)

rules = {}
rule_ids = []
for rule in tg.templates[provider]['rules_metadata']:
    rule_obj = CloudrailFormattedRule(rule, provider, tg.templates[provider])
    rules[rule_obj.get_id()] = rule_obj
    rule_ids.append(rule_obj.get_id())


@pytest.mark.parametrize("rule_id", rule_ids)
def test_rule(rule_id):
    """Tests rule"""
    rule_obj = rules[rule_id]
    assert rule_obj.check_terraform_code() is True
