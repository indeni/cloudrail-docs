from terraform_remediation_check import TerraformRemediationCheck


trc = TerraformRemediationCheck()


def test_rule():
    """Tests a rule using the remediation check"""
    rule_id = input('Enter rule_id: ')
    provider = input('Enter provider id: ')
    result = trc.check_rule(rule_id, provider, False)
    print(result)


if __name__ == '__main__':
    test_rule()
