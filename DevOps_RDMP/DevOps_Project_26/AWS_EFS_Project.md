# AWS Elastic File System (EFS) Project Guide

## Overview

Amazon EFS provides a scalable, fully managed elastic NFS file system for use with AWS Cloud services and on-premises resources. This guide documents the complete EFS setup with IAM permissions and network configuration.

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                            AWS CLOUD (us-west-1 N. California)                       │
│                                                                                      │
│  ┌─────────────────────────────────────────────────────────────────────────────┐    │
│  │                         VPC: Default (vpc-08cc0f47e139b54df)                 │    │
│  │                              CIDR: 172.31.0.0/16                              │    │
│  │                                                                               │    │
│  │   ┌─────────────────────────────────────────────────────────────────────┐    │    │
│  │   │                    EFS: mysystem (fs-029ad906463130926)              │    │    │
│  │   │                         Encrypted: ✅ Yes                            │    │    │
│  │   │                         Size: 6.00 KiB                               │    │    │
│  │   └─────────────────────────────────────────────────────────────────────┘    │    │
│  │                    │                              │                           │    │
│  │         ┌─────────┴──────────┐       ┌──────────┴─────────┐                  │    │
│  │         │   Mount Target 1   │       │   Mount Target 2   │                  │    │
│  │         │   AZ: us-west-1a   │       │   AZ: us-west-1c   │                  │    │
│  │         │   IP: 172.31.25.41 │       │   IP: 172.31.3.34  │                  │    │
│  │         │   subnet-04ae2ec   │       │   subnet-09ced74   │                  │    │
│  │         └─────────┬──────────┘       └──────────┬─────────┘                  │    │
│  │                   │                              │                            │    │
│  │         ┌─────────┴──────────────────────────────┴─────────┐                 │    │
│  │         │        Security Group: EFS-SG                     │                 │    │
│  │         │        (sg-00ca265c2656fd3e2)                     │                 │    │
│  │         │        Allows NFS traffic (Port 2049)             │                 │    │
│  │         └───────────────────────────────────────────────────┘                 │    │
│  │                                                                               │    │
│  │    ┌────────────────┐      ┌────────────────┐      ┌────────────────┐        │    │
│  │    │   EC2 Instance │      │   EC2 Instance │      │   EC2 Instance │        │    │
│  │    │   (AZ: 1a)     │      │   (AZ: 1c)     │      │   (Any AZ)     │        │    │
│  │    │   Mount EFS    │      │   Mount EFS    │      │   Mount EFS    │        │    │
│  │    └────────────────┘      └────────────────┘      └────────────────┘        │    │
│  │                                                                               │    │
│  └───────────────────────────────────────────────────────────────────────────────┘    │
│                                                                                      │
│  ┌──────────────────────────────────────────────────────────────────────────────┐   │
│  │                              IAM Configuration                                │   │
│  │   User: IAM_Punith                                                            │   │
│  │   Policies: EC2FullAccess, EFSFullAccess, VPCFullAccess, IAMFullAccess       │   │
│  └──────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                      │
│  Other VPCs Available:                                                               │
│  ├── MY cloud-vpc (vpc-001c72ca44f09fb81) - CIDR: 10.x.x.x                         │
│  └── on premises-vpc (vpc-0cf4fb1834013a019) - CIDR: 172.x.x.x                     │
│                                                                                      │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

---

## Project Components

| Component | Value | Description |
|-----------|-------|-------------|
| **EFS Name** | mysystem | Elastic File System for shared storage |
| **File System ID** | fs-029ad906463130926 | Unique identifier |
| **Region** | us-west-1 (N. California) | AWS Region |
| **Encryption** | Enabled | Data encrypted at rest |
| **IAM User** | IAM_Punith | User with EFS management permissions |
| **VPC** | vpc-08cc0f47e139b54df | Default VPC for EFS |
| **Security Group** | EFS-SG (sg-00ca265c2656fd3e2) | Controls NFS access |

---

## Prerequisites

- AWS Account with appropriate permissions
- Understanding of VPC, Subnets, and Security Groups
- EC2 instances to mount EFS

---

## Step 1: Create IAM User with Required Permissions

> IAM user needs proper policies to manage EFS and related resources.

### 1.1 Create IAM User

1. Go to **IAM Console** → **Users** → **Create user**
2. Enter username: `IAM_Punith`
3. Enable **AWS Management Console access**
4. Click **Next**

### 1.2 Attach Required Policies

| Policy Name | Type | Purpose |
|-------------|------|---------|
| `AmazonEC2FullAccess` | AWS Managed | Manage EC2 instances to mount EFS |
| `AmazonElasticFileSystemFullAccess` | AWS Managed | Full EFS management |
| `AmazonVPCFullAccess` | AWS Managed | Manage VPC and networking |
| `IAMFullAccess` | AWS Managed | Manage IAM resources |
| `EC2InstanceConnect` | AWS Managed | Connect to EC2 via browser |
| `IAMUserSSHKeys` | AWS Managed | Manage SSH keys |
| `AmazonConnect_FullAccess` | AWS Managed | Amazon Connect service |

### Your IAM User Setup:
```
User: IAM_Punith
├── AmazonConnect_FullAccess (AWS Managed) - Directly Attached
├── AmazonEC2FullAccess (AWS Managed) - Directly Attached
├── AmazonElasticFileSystemFullAccess (AWS Managed) - Directly Attached
├── AmazonVPCFullAccess (AWS Managed) - Directly Attached
├── EC2InstanceConnect (AWS Managed) - Directly Attached
├── IAMFullAccess (AWS Managed) - Directly Attached
└── IAMUserSSHKeys (AWS Managed) - Directly Attached
```

---

## Step 2: Create Security Group for EFS

> Security group controls which instances can access the EFS file system.

1. Go to **EC2 Console** → **Security Groups** → **Create Security Group**
2. Configure:

| Setting | Value |
|---------|-------|
| Name | `EFS-SG` |
| Description | Security group for EFS mount targets |
| VPC | Default VPC (vpc-08cc0f47e139b54df) |

3. **Inbound Rules:**

| Type | Protocol | Port | Source | Description |
|------|----------|------|--------|-------------|
| NFS | TCP | 2049 | 0.0.0.0/0 or specific SG | Allow NFS traffic |

4. Click **Create Security Group**

### Your Security Group:
```
Security Group: EFS-SG
ID: sg-00ca265c2656fd3e2
VPC: vpc-08cc0f47e139b54df (default)
Inbound: NFS (TCP 2049) from allowed sources
```

---

## Step 3: Create EFS File System

1. Go to **EFS Console** → **Create file system**
2. Click **Customize** for advanced options
3. Configure:

### General Settings:

| Setting | Value |
|---------|-------|
| Name | `mysystem` |
| Storage class | Standard |
| Automatic backups | Enable/Disable as needed |
| Lifecycle management | Configure as needed |
| Encryption | ✅ **Enable encryption at rest** |

4. Click **Next**

### Network Settings:

| Setting | Value |
|---------|-------|
| VPC | Default VPC (vpc-08cc0f47e139b54df) |

5. Click **Next** → **Create**

### Your EFS File System:
```
Name: mysystem
File System ID: fs-029ad906463130926
Encrypted: ✅ Yes
Total Size: 6.00 KiB
Size in Standard: 6.00 KiB
Size in IA: 0 Bytes
Size in Archive: 0 Bytes
State: Available
```

---

## Step 4: Configure Mount Targets

> Mount targets allow EC2 instances in specific AZs to connect to EFS.

1. Go to **EFS Console** → Select `mysystem` → **Network** tab
2. Click **Manage**
3. Configure mount targets for each Availability Zone:

### Mount Target Configuration:

| Availability Zone | Subnet ID | IP Address | Security Group |
|-------------------|-----------|------------|----------------|
| us-west-1a | subnet-04ae2ec | 172.31.25.41 | EFS-SG (sg-00ca265c2656fd3e2) |
| us-west-1c | subnet-09ced74 | 172.31.3.34 | EFS-SG (sg-00ca265c2656fd3e2) |

4. Select **EFS-SG** security group for both mount targets
5. Click **Save**

### Your Mount Targets:
```
Mount Target 1:
├── AZ: us-west-1a
├── Subnet: subnet-04ae2ec
├── IP: 172.31.25.41
├── IP Type: IPv4 only
└── Security Group: EFS-SG

Mount Target 2:
├── AZ: us-west-1c
├── Subnet: subnet-09ced74
├── IP: 172.31.3.34
├── IP Type: IPv4 only
└── Security Group: EFS-SG
```

---

## Step 5: VPC Configuration

### Your Available VPCs:

| VPC Name | VPC ID | State | CIDR Block |
|----------|--------|-------|------------|
| MY cloud-vpc | vpc-001c72ca44f09fb81 | Available | 10.x.x.x/16 |
| on premises-vpc | vpc-0cf4fb1834013a019 | Available | 172.x.x.x/16 |
| Default (no name) | vpc-08cc0f47e139b54df | Available | 172.31.0.0/16 |

> **Note:** EFS is configured in the Default VPC. If you need EFS access from other VPCs, you can use VPC Peering or Transit Gateway.

---

## Step 6: Mount EFS on EC2 Instance

### 6.1 Launch EC2 Instance

1. Launch an EC2 instance in the same VPC as EFS
2. Ensure the instance security group allows outbound NFS (port 2049)

### 6.2 Install EFS Mount Helper

```bash
# For Amazon Linux 2
sudo yum install -y amazon-efs-utils

# For Ubuntu
sudo apt-get update
sudo apt-get install -y amazon-efs-utils
```

### 6.3 Create Mount Point

```bash
sudo mkdir /mnt/efs
```

### 6.4 Mount EFS Using EFS Mount Helper (Recommended)

```bash
# Mount with encryption in transit
sudo mount -t efs -o tls fs-029ad906463130926:/ /mnt/efs

# OR without encryption
sudo mount -t efs fs-029ad906463130926:/ /mnt/efs
```

### 6.5 Mount EFS Using NFS Client

```bash
# Install NFS client
sudo yum install -y nfs-utils  # Amazon Linux
sudo apt-get install -y nfs-common  # Ubuntu

# Mount using NFS
sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport fs-029ad906463130926.efs.us-west-1.amazonaws.com:/ /mnt/efs
```

### 6.6 Verify Mount

```bash
df -h /mnt/efs
```

### 6.7 Auto-Mount on Reboot

Add to `/etc/fstab`:

```bash
# Using EFS mount helper
fs-029ad906463130926:/ /mnt/efs efs defaults,_netdev 0 0

# Using NFS
fs-029ad906463130926.efs.us-west-1.amazonaws.com:/ /mnt/efs nfs4 nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport,_netdev 0 0
```

---

## Step 7: Test EFS

### Create Test File

```bash
# On Instance 1
sudo touch /mnt/efs/test-file.txt
echo "Hello from Instance 1" | sudo tee /mnt/efs/test-file.txt
```

### Verify on Another Instance

```bash
# On Instance 2 (same EFS mounted)
cat /mnt/efs/test-file.txt
# Output: Hello from Instance 1
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Mount timeout | Check security group allows NFS (2049) inbound |
| Permission denied | Verify IAM permissions and security groups |
| DNS resolution failed | Ensure VPC DNS hostnames enabled |
| Mount helper not found | Install amazon-efs-utils package |

### Useful Commands:

```bash
# Check EFS mount status
mount | grep efs

# Check NFS connections
netstat -an | grep 2049

# Debug mount issues
sudo mount -t efs -o tls,mounttargetip=172.31.25.41 fs-029ad906463130926:/ /mnt/efs

# Unmount EFS
sudo umount /mnt/efs
```

---

## Cleanup / Delete Resources

> **Important:** Delete resources in the correct order.

### Deletion Order:

| Step | Resource | Action |
|------|----------|--------|
| 1 | Unmount EFS | Unmount from all EC2 instances |
| 2 | EC2 Instances | Terminate instances (optional) |
| 3 | EFS File System | Delete the file system |
| 4 | Security Group | Delete EFS-SG |
| 5 | IAM User | Delete user (if no longer needed) |

### Delete EFS:

1. **EFS Console** → Select `mysystem`
2. Click **Delete**
3. Enter file system ID to confirm: `fs-029ad906463130926`

---

## Summary

| Step | Action |
|------|--------|
| 1 | Create IAM User (IAM_Punith) with required policies |
| 2 | Create Security Group (EFS-SG) allowing NFS traffic |
| 3 | Create EFS File System (mysystem) with encryption |
| 4 | Configure Mount Targets in multiple AZs |
| 5 | Configure VPC networking |
| 6 | Mount EFS on EC2 instances |
| 7 | Test file sharing across instances |

---

## Key Information Reference

```
┌─────────────────────────────────────────────────────────────┐
│                    QUICK REFERENCE                          │
├─────────────────────────────────────────────────────────────┤
│ EFS File System ID : fs-029ad906463130926                   │
│ EFS Name           : mysystem                               │
│ Region             : us-west-1 (N. California)              │
│ VPC                : vpc-08cc0f47e139b54df                  │
│ Security Group     : sg-00ca265c2656fd3e2 (EFS-SG)          │
│ IAM User           : IAM_Punith                             │
│                                                             │
│ Mount Target 1 (us-west-1a): 172.31.25.41                   │
│ Mount Target 2 (us-west-1c): 172.31.3.34                    │
│                                                             │
│ Mount Command:                                              │
│ sudo mount -t efs fs-029ad906463130926:/ /mnt/efs           │
│                                                             │
│ DNS Name:                                                   │
│ fs-029ad906463130926.efs.us-west-1.amazonaws.com            │
└─────────────────────────────────────────────────────────────┘
```

---

**Author:** Darshan Raja  
**Last Updated:** March 2026
