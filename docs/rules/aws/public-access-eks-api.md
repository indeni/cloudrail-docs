# Ensure EKS API is not publicly accessible

*Amazon Web Services (AWS) > Kubernetes*

![Cloudrail and Amazon Web Services (AWS) logos](../images/cloudrail_aws.png)

## Details
The EKS cluster's management API is a sensitive endpoint to expose publicly. Cloudrail will determine if such an exposure occurred.

- **Severity**: 🔴 Major
- **Provider**: Amazon Web Services (AWS)
- **Category**: Kubernetes
- **Rule ID**: public_access_eks_api

---

## Remediation
Information on how to fix "Ensure EKS API is not publicly accessible" using available methods.


####  <img src="../_media/emojis/terraform.png" alt="terraform" width="20"/>  Terraform
For the aws_eks_cluster resource, in vpc_config block, set endpoint_public_access argument to false.








#### <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Cloudformation
For the AWS::EKS::Cluster resource, in ResourcesVpcConfig block, set EndpointPublicAccess argument to false.



####  <img src="../_media/emojis/aws.png" alt="aws" width="20"/> Console
Follow the guide at <https://aws.amazon.com/premiumsupport/knowledge-center/eks-public-private-access-api-server/> to configure private access to the EKS API.




---

## How It Works
Cloudrail will review all of the EKS clusters configured in your environment. For each cluster, it will review the whether the API has a public IP and whether it is Internet-accessible on the subnets it’s attached to. This determination will take into account the security groups, subnet information, routing and other information, instead of relying solely on the existence of a public IP address. By doing this context-based analysis, Cloudrail ensures that only EKS clusters whose API can truly be accessed from the Internet are highlighted.