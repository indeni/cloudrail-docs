# Ensure Config aggregator is enabled in all regions

*Amazon Web Services (AWS) > Logging*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Cloudrail will review the Config aggregator configuration in your environment. If it is not enabled in all regions, Cloudrail will highlight it as a violation.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Logging
- **Rule ID**: non_car_config_aggregator_is_enabled_in_all_regions

---

## Remediation
Information on how to fix "Ensure Config aggregator is enabled in all regions" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_config_configuration_aggregator resource, in the account_aggregation_source or organization_aggregation_source blocks, set the all_regions parameter to true.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::Config::ConfigurationAggregator resource, in AccountAggregationSources or OrganizationAggregationSource blocks, set AllAwsRegions argument to true.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/config/latest/developerguide/setup-aggregator-console.html> to enable Config aggregator in all regions.




---

## How It Works
Cloudrail will review the Config aggregator configuration within your AWS account and Terraform plan to check if it is enabled in all regions either at account level or at organization level.