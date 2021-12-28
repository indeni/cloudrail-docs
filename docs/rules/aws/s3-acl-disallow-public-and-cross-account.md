# Ensure S3 buckets are not made widely accessible through ACLs and bucket policies

*Amazon Web Services (AWS) > Storage*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
Generally, all S3 buckets, with specific exceptions, should not be publicly accessible. Access should be permitted only to specific entities and services, through tightly controlled policies.

- **Severity**: 🔴 Major
- **Provider**: Amazon Web Services (AWS)
- **Category**: Storage
- **Rule ID**: s3_acl_disallow_public_and_cross_account

---

## Remediation
Information on how to fix "Ensure S3 buckets are not made widely accessible through ACLs and bucket policies" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_s3_bucket resource, set the acl or grant arguments to restrict public access using an ACL, and set the policy argument to use a bucket policy that restricts public access. Additionally, if aws_s3_bucket_policy resource is being used, set policy argument to use a policy that restricts public access.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::S3::Bucket resource, set AccessControl argument to use a canned ACL that restricts public access. For the associated AWS::S3::BucketPolicy resource, set the PolicyDocument argument to use a policy that restricts public access.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/AmazonS3/latest/user-guide/set-bucket-permissions.html> to modify the S3 bucket ACL, and <https://docs.aws.amazon.com/AmazonS3/latest/user-guide/add-bucket-policy.html> to modify the S3 bucket policy.




---

## How It Works
Cloudrail will review the S3 buckets being created in your environment. For each bucket, it will analyze its ACLs and bucket policies. If an S3 bucket is allowing public access through an ACL (whether canned or user provided), or it is allowing cross-account access through ACL, or is allowing either of the above through a bucket policy, Cloudrail will highlight it as a violation.