# Ensure VPC Endpoint for S3 is enabled in all VPCs

*Amazon Web Services (AWS) > Storage*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
A best practice is to enforce the use of VPC Endpoints to avoid the need of sending data destined to S3 through the internet.

- **Severity**: 🔴 Major
- **Provider**: Amazon Web Services (AWS)
- **Category**: Storage
- **Rule ID**: vpc_endpoint_s3_exposure

---

## Remediation
Information on how to fix "Ensure VPC Endpoint for S3 is enabled in all VPCs" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
Create the aws_vpc_endpoint resource for the corresponding VPC to associate the S3 endpoint. Create the aws_vpc_endpoint_route_table_association resource in order to populate the route table with routes to the S3 service.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
Create the AWS::EC2::VPCEndpoint resource for the corresponding VPC to associate the S3 endpoint and set the RouteTableIds argument in order to populate the route table with routes to the S3 service.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-s3.html> to configure S3 endpoint for the VPC.




---

## How It Works
Cloudrail will identify all buckets and the regions where they exist. For each region, it will check that there is a VPC Endpoint for S3 created and which VPC it's associated to, it will then check all VPCs to identify which ones are not associated to a VPC Endpoint for S3 and will flag it as non-compliant, also if there were no VPC Endpoints in the region but there was a bucket it will flag all VPCs as non-compliant. It will check that there is at least one resource using an ENI to avoid alerting on unused VPCs.