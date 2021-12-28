# S3 Bucket is exposed via an overly permissive Lambda Execution Role

*Amazon Web Services (AWS) > IAM*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Excess of permissions in a Lambda Function can lead to inadvertently exposed resources such as S3 buckets. Best practices suggest use of least privileges - listing specific S3 buckets the Lambda Function is allowed to access. The Execution Role must be least privilege as an attacker can potentially access other S3 buckets if the application is exploited.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: IAM
- **Rule ID**: s3_lambda_indirect_exposure

---

## Remediation
Information on how to fix "S3 Bucket is exposed via an overly permissive Lambda Execution Role" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
Locate the aws_iam_policy resource associated to execution role of the Lambda Function and set the actions and resources to the minimum possible, avoiding the use of wildcards.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
Locate the AWS::IAM::Policy resource associated to execution role of the Lambda Function and set the actions and resources to the minimum possible, avoiding the use of wildcards.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Limit the actions and resources in the execution role policy of Lambda Function to the minimum possible, avoiding the use of wildcards.




---

## How It Works
Cloudrail will check if there is an API Gateway that's publicly accesible, if so it will also check for the existence of Lambda Functions that can be invoked by any of those API Gateways and if there is any it will check the execution role in the Lambda Function to verify if access to S3 is not limited to certain buckets, Cloudrail will also consider the bucket policy to flag only those buckets that can be accessed by the Lambda Function.