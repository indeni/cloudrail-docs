import os
import logging
import shutil
import yaml
import jinja2
import pytest

from cloudrail_formatted_rule import CloudrailFormattedRule
from terraform_remediation_check import TerraformRemediationCheck


class TemplateGenerator():
    """Template generator for Cloudrail templates"""

    def __init__(self):
        """Instantiate the module"""
        self._set_templates()
        self._copy_overview()
        self.templates = {}
        self.rules = {}

    def _get_yaml_file(self, file_path):
        """Returns an opened YAML file path"""
        with open(file_path) as file:
            try:
                return yaml.safe_load(file)
            except yaml.YAMLError as err:
                logging.error(err)

    def _get_cloud_yaml_files(self):
        """Retrieves all cloud yaml files"""
        self.yaml_aws = self._get_yaml_file('knowledge/cloudrail/knowledge/rules/aws/aws_rules_metadata.yaml')
        self.yaml_gcp = self._get_yaml_file('knowledge/cloudrail/knowledge/rules/gcp/gcp_rules_metadata.yaml')
        self.yaml_azure = self._get_yaml_file('knowledge/cloudrail/knowledge/rules/azure/azure_rules_metadata.yaml')

    def _set_templates(self):
        """Sets the templates from the filesystem"""
        template_path = 'templates/rule.template.md'
        with open(template_path) as template:
            self.rule_template = template.read()
        template_path = 'templates/overview.md'
        with open(template_path) as template:
            self.overview_template = template.read()
        template_path = 'templates/provider_overview.md'
        with open(template_path) as template:
            self.provider_overview_template = template.read()

    def _append_rule(self, rule):
        """Appends a rule to the list for overview readme generation"""
        if not self.rules.get(rule.provider):
            self.rules[rule.provider] = []
        self.rules[rule.provider].append(rule.serialize())

    def _create_provider_dir(self, provider):
        """Creates the provider directory if not already created"""
        os.makedirs(f'output/{provider}', exist_ok=True)
    
    def _copy_provider_img(self, provider):
        """Copies provider images"""
        os.makedirs(f'output/images', exist_ok=True)
        destination = f'output/images/cloudrail_{provider}.png'
        source = f'templates/images/cloudrail_{provider}.png'
        shutil.copy(source, destination)

    def _copy_overview(self):
        """Copies overview readme"""
        destination = f'output/overview.md'
        source = f'templates/overview.md'
        shutil.copy(source, destination)

    def _generate_rule_slug(self, rule):
        """Generates the slug from the rule"""
        return rule['rule_id'].replace('_', '-')
    
    def _render_intra_rule_field(self, field, provider):
        """Renders an intra rule field template if exists"""
        if type(field) == str:
            return field
        # Otherwise, render
        templates = {}
        for t in self.templates[provider]['templates']:
            templates.update(t)
        template = templates[field['template']]
        if not field.get('params'):
            return template
        return template.format(*field['params'])

    def _create_rule(self, rule, provider):
        """Creates the rule"""
        rule_obj = CloudrailFormattedRule(rule, provider, self.templates[provider])
        self._append_rule(rule_obj)
        t = jinja2.Template(self.rule_template)
        rendered = t.render(rule=rule_obj)
        fp = f'output/{provider}/{rule_obj.slug}.md'
        with open(fp, 'w') as outfile:
            outfile.write(rendered)

    def _render_rules(self, provider):
        """Renders rules for that particular provider"""
        self._create_provider_dir(provider)
        self._copy_provider_img(provider)
        fp = f'knowledge/cloudrail/knowledge/rules/{provider}/{provider}_rules_metadata.yaml'
        self.templates[provider] = self._get_yaml_file(fp)
        for rule in self.templates[provider]['rules_metadata']:
            self._create_rule(rule, provider)
        self._generate_provider_overview(provider)
    
    def _get_provider_pretty_name(self, provider):
        """Returns the pretty name of the provider"""
        return {
            'gcp': 'Google Cloud Platform (GCP)',
            'aws': 'Amazon Web Services (AWS)',
            'azure': 'Microsoft Azure',
        }[provider]

    def _generate_provider_overview(self, provider):
        """Generates an overview readme for the provider"""
        args = {}
        t = jinja2.Template(self.provider_overview_template)
        pretty_provider = self._get_provider_pretty_name(provider)
        rendered = t.render(rules=self.rules[provider], provider=provider, pretty_provider=pretty_provider)
        fp = f'output/{provider}/overview.md'
        with open(fp, 'w') as outfile:
            outfile.write(rendered)

    def generate(self):
        """Generates the repository structure"""
        self._render_rules('gcp')
        self._render_rules('aws')
        self._render_rules('azure')
    
    def _generate_test_rule_structure(rule_id, provider):
        """Generate the test rule structure for the rule"""
        return rule_id, provider
    
    def test(self):
        """Runs tests on rules"""
        self.templates[provider] = self._get_yaml_file(fp)
        self.remediation_checker = TerraformRemediationCheck()
        rules = []
        for rule in self.templates[provider]['rules_metadata']:
            rules.append(rule['rule_id'], provider)

        @pytest.mark.parametrize("rule_id, provider", rules)
        def test_rule(rule_id, provider):
            """Tests rule"""
            assert self.remediation_checker.check_rule(rule_id, provider) is True


if __name__ == "__main__":
    tg = TemplateGenerator()
    tg.generate()
