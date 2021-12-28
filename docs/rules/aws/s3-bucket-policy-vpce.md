# Ensure that the private bucket's policy reference a VPC Endpoint as source

*Amazon Web Services (AWS) > Service Endpoints, IAM*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
In an environment where VPC Endpoints are used for S3, and private S3 buckets are created, it’s important to consider the use of a source VPCE condition in the bucket policy. Often times, this will be missed, which means that an attacker can use stolen credentials outside of your VPCs.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Service Endpoints, IAM
- **Rule ID**: s3_bucket_policy_vpce

---

## Remediation
Information on how to fix "Ensure that the private bucket's policy reference a VPC Endpoint as source" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_s3_bucket_policy resource, modify policy argument to include a condition "aws:SourceVpce" in order to restrict access to a specific VPC endpoint.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::S3::BucketPolicy resource, modify PolicyDocument block to include a condition "aws:SourceVpce" in order to restrict access to a specific VPC endpoint.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies-vpc-endpoint.html> to modify S3 bucket policy and restrict access to a specific VPC endpoint.




---

## How It Works
First check if there is a bucket in the region, if so check that at least one VPC Endpoint for S3 exists. Then, for each private bucket in the region get the policy and check if a condition which contains the string "aws:SourceVpce" which would indicate that the policy is limiting the source of the requests.