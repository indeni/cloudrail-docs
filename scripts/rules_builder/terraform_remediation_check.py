import os
import logging
import shutil
import json
import subprocess


class TerraformRemediationCheck():
    """Module for checking all terraform docs to ensure they're correct"""

    def __init__(self):
        """Instantiate the module"""
        logging.basicConfig(level=logging.INFO)
        self._set_defaults()

    def _set_defaults(self):
        """Sets defaults for the module"""
        self.temp_check_dir = '/tmp/tf_check_dir/'
        self.cloudrail_output_file = '/tmp/tf_check_dir/output.json'

    def check_rule(self, rule_id, provider, null=True):
        """Checks a rule's terraform docs to ensure it's been verified
            Returns True, False, or None
        """
        logging.info(f'Checking {rule_id} - {provider}')
        self._create_temp_dir()
        fp_vuln = self._get_tf_file_path(rule_id, provider, 'vulnerable')
        fp_fixed = self._get_tf_file_path(rule_id, provider, 'fixed')
        if not fp_fixed or not fp_vuln:
            self._delete_temp_dir()
            return None
        # Check vulnerable rule first
        self._copy_file_to_temp_dir(fp_vuln)
        self._run_cloudrail(rule_id, null)
        if not null:
            self._cat_file()
        results_vuln = self._check_json_is_rule_violated(rule_id)
        self._delete_temp_dir()
        if results_vuln is None:
            return None
        if results_vuln is False:
            return False
        # Check fixed rule
        self._create_temp_dir()
        self._copy_file_to_temp_dir(fp_fixed)
        self._run_cloudrail(rule_id, null)
        if not null:
            self._cat_file()
        results_fixed = self._check_json_is_rule_violated(rule_id)
        self._delete_temp_dir()
        if results_fixed is None:
            return None
        if results_fixed is True:
            return False
        return True

    def _check_json_is_rule_violated(self, rule_id):
        """Checks JSON for rule violation"""
        try:
            with open(self.cloudrail_output_file) as file:
                rules = json.loads(file.read())
        except Exception:
            return None
        for r in rules:
            if r['rule_id'] == rule_id:
                if r['status'] == 'failed':
                    return True
                elif r['status'] == 'success':
                    return False
                else:
                    return None
    
    def _cat_file(self, keyword=None):
        """Cats the file"""
        cmd = f"cat {self.cloudrail_output_file}"
        if keyword:
            cmd = cmd +  f" | grep {keyword}"
        subprocess.call(cmd, shell=True)

    def _run_cloudrail(self, rule_id, null):
        """Runs cloudrail on the directory"""
        cmd = f'cd {self.temp_check_dir} && cloudrail run -o json --auto-approve -f {self.cloudrail_output_file}'
        if null:
            subprocess.call(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        else:
            subprocess.call(cmd, shell=True)

    def _create_temp_dir(self):
        """Creates a temporary directory for verification"""
        os.makedirs(self.temp_check_dir, exist_ok=True)

    def _delete_temp_dir(self):
        """Deletes the temporary directory"""
        shutil.rmtree(self.temp_check_dir)

    def _copy_file_to_temp_dir(self, file_path):
        """Copies the file to the tempdir"""
        shutil.copy(file_path, self.temp_check_dir)

    def _get_base_rules_path(self):
        """Returns the base rules path"""
        return 'knowledge/cloudrail/knowledge/rules'

    def _get_tf_file_path(self, rule_id, provider, code_type='fixed'):
        """Returns the vulnerable file path for the rule or None"""
        base = self._get_base_rules_path()
        fp = f"{base}/{provider}/metadata/terraform/{rule_id}.{code_type}.tf"
        if os.path.exists(fp):
            return fp
        return None
