# Cloudrail Rules - Google Cloud Platform (GCP)
Cloudrail rules for Google Cloud Platform (GCP), click on a rule for more details and how to fix it.

| Severity | Category | Name |
| ----------- | ----------- | ----------- |
 | 🔴 | Database | [Ensure SQL database requires SSL](rules/gcp/non-car-gcp-sql-database-ssl-required) |
 | 🔴 | Database | [Ensure that Cloud SQL database instances are not open to the world](rules/gcp/non-car-cloud-sql-restrict-trusted-ip) |
 | 🟡 | Database | [Ensure that Cloud SQL database instances do not have public IPs](rules/gcp/non-car-cloud-sql-database-instance-no-public-ip) |
 | 🔴 | Compute | [Ensure ‘Enable connecting to serial ports’ is not enabled for VM Instance](rules/gcp/non-car-compute-instance-ensure-serial-port-disabled) |
 | 🟡 | Compute | [Ensure Compute instances are launched with Shielded VM enabled](rules/gcp/non-car-compute-instance-ensure-shielded-vm) |
 | 🔴 | Compute | [Ensure that Compute instances do not have public IP addresses](rules/gcp/non-car-compute-instance-ensure-no-public-ip) |
 | 🟡 | Database | [Ensure that all Cloud SQL database instances have backup configuration enabled](rules/gcp/non-car-cloud-sql-enable-backup) |
 | 🟡 | Compute | [Ensure that instances are not configured to use the default service account](rules/gcp/non-car-compute-instance-no-default-service-account) |
 | 🟡 | Database | [Ensure SQL database ‘contained database authentication’ flag is set to ‘off’](rules/gcp/non-car-cloud-sql-contained-database-authentication-off) |
 | 🟡 | Database | [Ensure SQL database ‘cross db ownership chaining’ flag is set to ‘on'](rules/gcp/non-car-cloud-sql-crossdb-ownership-chaining-on) |
 | 🟡 | Compute | [Ensure that instances are not configured to use the default service account with full access to all Cloud APIs](rules/gcp/non-car-compute-instance-no-default-service-account-full-access-api) |
 | 🟡 | Compute | [Ensure that IP forwarding is not enabled on Instances](rules/gcp/non-car-compute-instance-ensure-no-ip-forwarding) |
 | 🟡 | Database | [Ensure PostgreSQL database ‘log_min_duration_statement’ flag is set to -1](rules/gcp/non-car-cloud-sql-log-min-duration-disable) |
 | 🟡 | Database | [Ensure PostgreSQL database ‘log_temp_files’ flag is set to 0](rules/gcp/non-car-cloud-sql-log-temp-files-zero) |
 | 🟡 | Database | [Ensure PostgreSQL database log_lock_waits flag is set to on](rules/gcp/non-car-cloud-sql-log-lock-waits-on) |
 | 🟡 | Database | [Ensure PostgreSQL database ‘log_disconnections’ flag is set to ‘on’](rules/gcp/non-car-cloud-sql-log-disconnections-on) |
 | 🔴 | Kubernetes | [Ensure GKE Control Plane is not public](rules/gcp/non-car-gke-control-plane-ensure-not-public) |
 | 🟡 | Database | [Ensure PostgreSQL database ‘log_connections’ flag is set to ‘on’](rules/gcp/non-car-cloud-sql-log-connections-on) |
 | 🟡 | Database | [Ensure PostgreSQL database ‘log_checkpoints’ flag is set to ‘on’](rules/gcp/non-car-cloud-sql-log-checkpoints-on) |
 | 🟡 | Database | [Ensure PostgreSQL database ‘log_min_error_statement’ flag is set to a valid value](rules/gcp/non-car-cloud-sql-log-min-error) |
 | 🟡 | Storage | [Ensure that logging is enabled for cloud storage buckets](rules/gcp/non-car-storage-bucket-ensure-logging-enabled) |
 | 🟡 | Network | [Ensure that RSASHA1 is not used for the zone-signing and key-signing keys in Cloud DNS DNSSEC](rules/gcp/non-car-cloud-dns-ensure-rsasha1-disabled) |
 | 🔴 | Network | [Ensure no HTTPS or SSL proxy load balancers permit SSL policies with weak cipher suites](rules/gcp/car-proxy-lb-ssl-policy-no-weak-ciphers) |
 | 🟡 | Logging | [Ensure that VPC Flow Logs is enabled for every subnet in a VPC Network](rules/gcp/non-car-compute-subnetwork-ensure-vpc-flow-logs-enabled) |
 | 🟡 | Kubernetes | [Manage Kubernetes RBAC users with Google Groups for GKE](rules/gcp/non-car-gke-manage-rbac-users-with-google-groups) |
 | 🔴 | Network | [Ensure Compute Resources are not publicly accessible via SSH](rules/gcp/car-vpc-not-publicly-accessible-ssh) |
 | 🔴 | Network | [Ensure Compute Resources are not publicly accessible via RDP](rules/gcp/car-vpc-not-publicly-accessible-rdp) |
 | 🔴 | IAM | [Ensure that Cloud Storage bucket is not anonymously or publicly accessible](rules/gcp/car-storage-bucket-ensure-no-anonymous-public-access) |
