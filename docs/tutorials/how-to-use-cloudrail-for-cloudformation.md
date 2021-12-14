# How to use Cloudrail with AWS Cloudformation Templates
In this tutorial, we will use Indeni Cloudrail to scan AWS Cloudformation templates for security vulnerabilities that might be present.

## Prerequisites
You will first need to connect your cloud account to cloudrail, and retrieve the cloud-account-id from the cloudrail console.

First, we'll use an example template provided by AWS, located [here](https://s3.us-west-2.amazonaws.com/cloudformation-templates-us-west-2/EC2InstanceWithSecurityGroupSample.template).

Create a sample folder, and download the template to it.

```bash
mkdir cloudformation_test
cd cloudformation_test
curl https://s3.us-west-2.amazonaws.com/cloudformation-templates-us-west-2/EC2InstanceWithSecurityGroupSample.template > sample.json
```

Next, find the cloud_account_id of the cloud account you're planning on deploying this stack to:

```bash
cloudrail cloud-account list-cloud-accounts
```

```txt
name                                             cloud_account_id                      status    last_collected_at
example-account                                  123456789012                          ready     2021-11-24 15:47:28Z
```

We'll also need a parameters file for this particular template, defining the name of a hypothetical key-pair for connecting to the EC2 instance.

```bash
cat << EOF > ./sample.params.json
[
    {
        "ParameterKey":"KeyName",
        "ParameterValue":"sample-key"
    }
]
EOF
```


Next, run Cloudrail within the directory to perform a dynamic assessment, inputting your cloud account.

```bash
# Replace --cloud-account-id 123456789012 with your cloud account ID
cloudrail run \
    -c sample.json \
    --cfn-params-file sample.params.json \
    --cloud-account-id 123456789012 \
    --auto-approve
```
