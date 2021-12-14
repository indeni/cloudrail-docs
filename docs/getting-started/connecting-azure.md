# Connecting Microsoft Azure to Cloudrail

![Microsoft Azure logo](../_media/integrations/cloudrail_azure.png)

## How To Connect Cloudrail To Your Microsoft Azure Account
1. In the cloudrail web application, navigate to `Environments`, then the [Live Environment tab](https://web.cloudrail.app/environments/live-environment).

2. Click the ["Add Account" button](https://web.cloudrail.app/add-account) to be taken to the add account wizard.

3. Select `Microsoft Azure` as your cloud provider.

4. Follow the on-screen instructions to create a Cloudformation stack. Cloudrail will provide a link to launch a CloudFormation stack with the required information automatically populated.

![Connecting Azure Screenshot](../_media/screenshots/connect_azure.png)

## How It Works
Cloudrail connects through an Active Directory application, which needs to be provided with the Reader role. From here, cloudrail can audit the account for misconfigurations and drift.

---

## Next Steps
Next, check out how to [add custom rules and policies for your environments](getting-started/defining-policies.md).
