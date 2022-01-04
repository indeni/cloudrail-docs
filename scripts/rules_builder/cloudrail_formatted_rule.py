import os
import datetime
import logging
from terraform_remediation_check import TerraformRemediationCheck


class CloudrailFormattedRule():
    """Class for representing a formatted cloudrail rule"""

    def __init__(self, rule, provider, full_template):
        """Instantiate the rule"""
        self.raw = rule
        self.provider = provider
        self.full_template = full_template
        self.remediation_checker = TerraformRemediationCheck()
        self._format_rule()
    
    def _format_rule(self):
        """Formats the rule"""
        self.name = self.get_name()
        self.id = self.get_id()
        self.title = self.name
        self.category = self.get_resource_type()
        self.resource_types = self.get_resource_types()
        self.severity = self.get_severity_pretty()
        self.severity_emoji = self.get_severity_emoji()
        self.provider_image_url = self.get_provider_image_url()
        self.human_readable_logic = self.get_human_readable_logic()
        self.description = self.get_description()
        self.remediation = {
            'console': self.get_remediation_console(),
            'cloudformation': self.get_remediation_cloudformation(),
            'terraform': self.get_remediation_terraform(),
        }
        self.provider_pretty = self.get_provider_pretty_name()
        self.slug = self.get_slug()

    def get_name(self):
        """Return the name of the rule"""
        name = self._render_intra_rule_field(self.raw['name'])
        name = name.replace('`', '')
        return name

    def get_id(self):
        """Returns the rule ID"""
        return self.raw['rule_id']

    def _get_base_rules_path(self):
        """Returns the base rules path"""
        return 'knowledge/cloudrail/knowledge/rules'

    def get_terraform_code(self, code_type='fixed'):
        """Returns vulnerable terraform code, or none"""
        base = self._get_base_rules_path()
        fp = f"{base}/{self.provider}/metadata/terraform/{self.raw['rule_id']}.{code_type}.tf"
        if os.path.exists(fp):
            with open(fp) as file:
                return file.read()
        return None

    def get_cli_code(self):
        base = self._get_base_rules_path()
        fp = f"{base}/{self.provider}/metadata/cli/{self.raw['rule_id']}.sh"
        if os.path.exists(fp):
            with open(fp) as file:
                return file.read()
        return None

    def get_slug(self):
        """Returns the slug of the rule"""
        return self.get_id().replace('_', '-')
    
    def check_terraform_code(self):
        """Checks terraform code for a result"""
        result = self.remediation_checker.check_rule(self.get_id(), self.provider)
        if result is False:
            logging.error(f'FAIL - {self.get_id()}')
        if result is True:
            return True

    def get_remediation_terraform(self):
        """Returns terraform remediation"""
        if not self.raw['remediation_steps'].get('terraform'):
            return None
        rendered = self._render_intra_rule_field(self.raw['remediation_steps']['terraform'])
        return {
            'text': self._apply_general_filters(rendered),
            'code_vulnerable': self.get_terraform_code('vulnerable'),
            'code_fixed': self.get_terraform_code('fixed'),
        }

    def get_remediation_console(self):
        """Returns terraform remediation"""
        if not self.raw['remediation_steps'].get('console'):
            return None
        rendered = self._render_intra_rule_field(self.raw['remediation_steps']['console'])
        return {
            'text': self._apply_general_filters(rendered),
            'code': self.get_cli_code(),
        }

    def get_remediation_cloudformation(self):
        """Returns cloudformation remediation"""
        if not self.raw['remediation_steps'].get('cloudformation'):
            return None
        rendered = self._render_intra_rule_field(self.raw['remediation_steps']['cloudformation'])
        return {
            'text': self._apply_general_filters(rendered),
            'code_vulnerable': None, #TODO
            'code_fixed': None, #TODO
        }

    def get_description(self):
        """Returns the rule description"""
        desc = self._render_intra_rule_field(self.raw['description'])
        desc = self._apply_general_filters(desc)
        return desc

    def get_human_readable_logic(self):
        """Returns human readable logic"""
        hrl = self._render_intra_rule_field(self.raw['human_readable_logic'])
        hrl = self._apply_general_filters(hrl)
        return hrl

    def get_resource_types(self):
        """Returns the pretty name of the severity"""
        replacements = [
            ['Key_Mgmt', 'Key Management'],
            ['Iam', 'IAM'],
            ['Service_Endpoint', 'Service Endpoints'],
            ['Content_Delivery', 'Content Delivery'],
            ['Notification', 'Notifications'],
        ]
        finalized = []
        for rt in self.raw['resource_type']:
            temp = rt.title()
            for r in replacements:
                temp = temp.replace(r[0], r[1])
            finalized.append(temp)
        return ", ".join(finalized)

    def get_resource_type(self):
        """Returns the first resource type"""
        return self.raw['resource_type'][0]

    def get_severity_emoji(self):
        """Returns the severity emoji"""
        return {
            'medium': '🟡',
            'major': '🔴',
            'low': '🟢',
        }[self.raw['severity']]

    def get_severity_pretty(self):
        """Returns the pretty name of the severity"""
        return self.raw['severity'].title()

    def get_provider_image_url(self):
        """Returns the provider image URL"""
        return f'../images/cloudrail_{self.provider}.png'
    
    def _render_intra_rule_field(self, field):
        """Renders an intra rule field template if exists"""
        if type(field) == str:
            return field
        # Otherwise, render
        templates = {}
        for t in self.full_template['templates']:
            templates.update(t)
        template = templates[field['template']]
        if not field.get('params'):
            return template
        return template.format(*field['params'])

    def get_provider_pretty_name(self):
        """Returns the pretty name of the provider"""
        return {
            'gcp': 'Google Cloud Platform (GCP)',
            'aws': 'Amazon Web Services (AWS)',
            'azure': 'Microsoft Azure',
        }[self.provider]
    
    def _apply_general_filters(self, field):
        """Applies general filters to the field"""
        field = field.replace('0.0.0.0/0', '`0.0.0.0/0`')
        field = field.replace('::/0', '`::/0`')
        return field

    def serialize(self):
        """Returns a serialized dict"""
        return {
            'name': self.name,
            'title': self.title,
            'slug': self.slug,
            'category': self.category,
            'resource_types': self.resource_types,
            'severity': self.severity,
            'severity_emoji': self.severity_emoji,
            'provider_image_url': self.provider_image_url,
            'human_readable_logic': self.human_readable_logic,
            'description': self.description,
            'remediation': self.remediation,
        }
