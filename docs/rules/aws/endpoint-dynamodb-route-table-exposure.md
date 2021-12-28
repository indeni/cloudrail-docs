# Ensure VPC Endpoint for DynamoDB is enabled in all route tables in use in a VPC

*Amazon Web Services (AWS) > Storage*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
A best practice is to enforce the use of VPC Endpoints to avoid the need of sending data destined to DynamoDB through the internet. Cloudrail will identify misconfigurations and exposure by checking if VPC Endpoint Gateways are in use or not, by reviewing VPC Endpoint and route tables in all regions.

- **Severity**: 🟡 Medium
- **Provider**: Amazon Web Services (AWS)
- **Category**: Storage
- **Rule ID**: endpoint_dynamodb_route_table_exposure

---

## Remediation
Information on how to fix "Ensure VPC Endpoint for DynamoDB is enabled in all route tables in use in a VPC" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_vpc_endpoint_route_table_association resource, set the route_table_id and vpc_endpoint_id arguments for the DynamoDB service.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::EC2::VPCEndpoint resource, set the RouteTableIds for the DynamoDB service.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://docs.aws.amazon.com/vpc/latest/userguide/vpce-gateway.html#vpc-endpoints-routing> to configure the route tables to route DynamoDB service traffic via the endpoint.




---

## How It Works
Cloudrail will identify all tables and the regions where they exist. For each region, it will check that there is a VPC Endpoint for DynamoDB created, if so it will check which route tables it's associated to, it will then check all route tables to identify which ones are not associated to a VPC Endpoint for DynamoDB and will flag them as non-compliant. It will check the routing tables in each VPC to avoid alerting on subnets that don't have internet access.