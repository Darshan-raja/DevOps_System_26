# AWS Site-to-Site VPN Connection Setup Guide

## Overview

This guide walks you through creating a **Site-to-Site VPN connection** between an On-Premise network (simulated in AWS) and an AWS Cloud VPC.

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              AWS CLOUD                                       │
│                                                                              │
│  ┌──────────────────────────┐         ┌──────────────────────────┐          │
│  │   ON-PREMISE VPC         │   VPN   │      AWS CLOUD VPC       │          │
│  │   (172.16.0.0/16)        │ TUNNEL  │   (10.0.0.0/16)          │          │
│  │                          │◄───────►│                          │          │
│  │  ┌────────────────────┐  │         │  ┌────────────────────┐  │          │
│  │  │  Public Instance   │  │         │  │  Private Instance  │  │          │
│  │  │  (StrongSwan VPN)  │  │         │  │                    │  │          │
│  │  │  Public IP Enabled │  │         │  │  No Public IP      │  │          │
│  │  └────────────────────┘  │         │  └────────────────────┘  │          │
│  │                          │         │                          │          │
│  └──────────────────────────┘         └──────────────────────────┘          │
│           │                                      │                           │
│           │                                      │                           │
│   Customer Gateway                    Virtual Private Gateway                │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Key Components

| Component | Purpose |
|-----------|---------|
| **On-Premise VPC** | Simulates your on-premise data center |
| **AWS Cloud VPC** | Your main cloud infrastructure |
| **Customer Gateway** | Represents your on-premise VPN device |
| **Virtual Private Gateway** | AWS-managed VPN endpoint |
| **Site-to-Site VPN** | Encrypted tunnel between both networks |
| **StrongSwan** | Open-source IPsec VPN software |

---

## Prerequisites

- AWS Account with appropriate permissions
- Basic understanding of VPC, Subnets, and Security Groups
- SSH key pair for EC2 instances

---

## Step 1: Create On-Premise VPC

> This VPC simulates your on-premise data center network.

1. Go to **VPC Console** → Click **Create VPC**
2. Select **VPC and more**
3. Configure:

| Setting | Value |
|---------|-------|
| VPC Name | `On-Premise-VPC` |
| IPv4 CIDR Block | `172.16.0.0/16` |
| Availability Zones | `1` |
| Public Subnets | `1` |
| Private Subnets | `0` |
| NAT Gateways | `None` |
| VPC Endpoints | `None` |

4. Click **Create VPC**

---

## Step 2: Create AWS Cloud VPC

> This is your main AWS cloud infrastructure.

1. Go to **VPC Console** → Click **Create VPC**
2. Select **VPC and more**
3. Configure:

| Setting | Value |
|---------|-------|
| VPC Name | `AWS-Cloud-VPC` |
| IPv4 CIDR Block | `10.0.0.0/16` |
| Availability Zones | `1` |
| Public Subnets | `0` |
| Private Subnets | `1` |
| NAT Gateways | `None` |
| VPC Endpoints | `None` |

4. Click **Create VPC**

---

## Step 3: Create Public Instance (On-Premise - VPN Server)

> This instance will act as the VPN gateway using StrongSwan.

1. Go to **EC2 Console** → Click **Launch Instance**
2. Configure:

| Setting | Value |
|---------|-------|
| Name | `On-Premise-Public-Instance` |
| AMI | Amazon Linux 2 or Ubuntu |
| Instance Type | `t2.micro` |
| Key Pair | Create new or select existing |
| VPC | `On-Premise-VPC` |
| Subnet | Public Subnet |
| Auto-assign Public IP | **Enable** |

3. **Security Group Configuration** - Create `Public-SG`:

| Type | Protocol | Port Range | Source | Description |
|------|----------|------------|--------|-------------|
| SSH | TCP | 22 | 0.0.0.0/0 | SSH Access |
| Custom UDP | UDP | 500 | 0.0.0.0/0 | IKE (IPsec) |
| Custom UDP | UDP | 4500 | 0.0.0.0/0 | NAT-T (IPsec) |
| All ICMP - IPv4 | ICMP | All | 10.0.0.0/16 | Ping from AWS VPC |

4. Click **Launch Instance**
5. **Note down the Public IP address** (e.g., `X.X.X.X`)

---

## Step 4: Create Private Instance (AWS Cloud)

> This instance is in the private subnet and will communicate through VPN.

1. Go to **EC2 Console** → Click **Launch Instance**
2. Configure:

| Setting | Value |
|---------|-------|
| Name | `AWS-Cloud-Private-Instance` |
| AMI | Amazon Linux 2 or Ubuntu |
| Instance Type | `t2.micro` |
| Key Pair | Create new or select existing |
| VPC | `AWS-Cloud-VPC` |
| Subnet | Private Subnet |
| Auto-assign Public IP | **Disable** |

3. **Security Group Configuration** - Create `Private-SG`:

| Type | Protocol | Port Range | Source | Description |
|------|----------|------------|--------|-------------|
| SSH | TCP | 22 | 172.16.0.0/16 | SSH from On-Premise |
| All ICMP - IPv4 | ICMP | All | 172.16.0.0/16 | Ping from On-Premise |

4. Click **Launch Instance**

---

## Step 5: Create Customer Gateway

> The Customer Gateway represents your on-premise VPN device (the public instance).

1. Go to **VPC Console** → **Customer Gateways** → **Create Customer Gateway**
2. Configure:

| Setting | Value |
|---------|-------|
| Name | `On-Premise-CGW` |
| BGP ASN | `65000` (default) |
| IP Address | Public IP of On-Premise Instance |
| Device | Leave empty |

3. Click **Create Customer Gateway**

---

## Step 6: Create Virtual Private Gateway

> The Virtual Private Gateway is the AWS-managed VPN endpoint.

1. Go to **VPC Console** → **Virtual Private Gateways** → **Create Virtual Private Gateway**
2. Configure:

| Setting | Value |
|---------|-------|
| Name | `AWS-VPG` |
| Amazon default ASN | Use default |

3. Click **Create Virtual Private Gateway**
4. **Attach to VPC:**
   - Select the VPG → **Actions** → **Attach to VPC**
   - Select `AWS-Cloud-VPC`
   - Click **Attach**

---

## Step 7: Create Site-to-Site VPN Connection

1. Go to **VPC Console** → **Site-to-Site VPN Connections** → **Create VPN Connection**
2. Configure:

| Setting | Value |
|---------|-------|
| Name | `My-VPN-Connection` |
| Target Gateway Type | Virtual Private Gateway |
| Virtual Private Gateway | `AWS-VPG` |
| Customer Gateway | Existing |
| Customer Gateway ID | `On-Premise-CGW` |
| Routing Options | Static |
| Static IP Prefixes | `172.16.0.0/16` |

3. Click **Create VPN Connection**
4. Wait for the VPN to be created (takes 2-3 minutes)

---

## Step 8: Download VPN Configuration

1. Select the VPN Connection → **Download Configuration**
2. Choose:

| Setting | Value |
|---------|-------|
| Vendor | StrongSwan |
| Platform | Ubuntu |
| Software | StrongSwan |
| IKE Version | IKEv1 |

3. Download and save the configuration file

---

## Step 9: Configure StrongSwan on Public Instance

### 9.1 Connect to Public Instance and Install StrongSwan

```bash
# SSH into your public instance
ssh -i your-key.pem ec2-user@<PUBLIC_IP>

# Update and install StrongSwan (Ubuntu)
sudo apt update && sudo apt install strongswan -y

# For Amazon Linux
sudo yum install strongswan -y
```

### 9.2 Enable IP Forwarding

```bash
# Edit sysctl.conf
sudo nano /etc/sysctl.conf

# Uncomment or add this line:
net.ipv4.ip_forward=1

# Apply changes
sudo sysctl -p

# Verify
cat /proc/sys/net/ipv4/ip_forward
# Should output: 1
```

### 9.3 Configure IPsec (from downloaded config)

Edit the IPsec configuration file:

```bash
sudo nano /etc/ipsec.conf
```

Add the tunnel configuration from downloaded file. Example structure:

```conf
conn Tunnel1
    auto=start
    left=%defaultroute
    leftid=<YOUR_PUBLIC_IP>
    right=<AWS_VPN_ENDPOINT_1>
    type=tunnel
    leftauth=psk
    rightauth=psk
    keyexchange=ikev1
    ike=aes128-sha1-modp1024
    ikelifetime=8h
    esp=aes128-sha1-modp1024
    lifetime=1h
    keyingtries=%forever
    leftsubnet=172.16.0.0/16
    rightsubnet=10.0.0.0/16
    dpddelay=10s
    dpdtimeout=30s
    dpdaction=restart
    leftupdown="/etc/ipsec.d/aws-updown.sh -ln Tunnel1 -ll <LOCAL_TUNNEL_IP>/30 -lr <REMOTE_TUNNEL_IP>/30 -m 100 -r 10.0.0.0/16"
```

### 9.4 Configure IPsec Secrets

```bash
sudo nano /etc/ipsec.secrets
```

Add the pre-shared keys (from downloaded config):

```
# Tunnel 1
<YOUR_PUBLIC_IP> <AWS_ENDPOINT_1> : PSK "your-pre-shared-key-1"

# Tunnel 2
<YOUR_PUBLIC_IP> <AWS_ENDPOINT_2> : PSK "your-pre-shared-key-2"
```

### 9.5 Create AWS Updown Script

```bash
sudo nano /etc/ipsec.d/aws-updown.sh
```

Add the script content (from downloaded config) and make it executable:

```bash
sudo chmod 744 /etc/ipsec.d/aws-updown.sh
```

### 9.6 Start/Restart IPsec Service

```bash
# Restart IPsec
sudo ipsec restart

# Check status
sudo ipsec status

# View connection details
sudo ipsec statusall
```

---

## Step 10: Update Route Table for Private Subnet

1. Go to **VPC Console** → **Route Tables**
2. Select the route table associated with `AWS-Cloud-VPC` private subnet
3. Click **Edit routes** → **Add route**

| Destination | Target |
|-------------|--------|
| 172.16.0.0/16 | Virtual Private Gateway (`AWS-VPG`) |

4. Click **Save changes**

---

## Step 11: Test VPN Connection

### From Public Instance (On-Premise):

```bash
# Ping the private instance in AWS Cloud VPC
ping <PRIVATE_INSTANCE_PRIVATE_IP>
# Example: ping 10.0.1.50
```

### From Private Instance (AWS Cloud):

```bash
# First, connect via Session Manager or bastion
# Then ping the on-premise public instance private IP
ping <PUBLIC_INSTANCE_PRIVATE_IP>
# Example: ping 172.16.1.100
```

### Check VPN Status in AWS Console:

1. Go to **VPC Console** → **Site-to-Site VPN Connections**
2. Check **Tunnel Details** tab
3. Status should show **UP** for at least one tunnel

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Tunnel shows DOWN | Check Security Group UDP ports 500 & 4500 |
| Cannot ping across VPCs | Verify route tables have correct routes |
| IPsec service not starting | Check /var/log/syslog for errors |
| Connection timeout | Verify Customer Gateway IP is correct |

### Useful Commands:

```bash
# Check IPsec status
sudo ipsec status

# View detailed logs
sudo tail -f /var/log/syslog | grep -i ipsec

# Restart IPsec service
sudo ipsec restart

# Enable IP forwarding temporarily
sudo su
echo 1 > /proc/sys/net/ipv4/ip_forward
```

---

## Cleanup / Delete Resources

> **Important:** Delete resources in the correct order to avoid dependency errors.

### Deletion Order:

| Step | Resource | Action |
|------|----------|--------|
| 1 | EC2 Instances | Terminate both instances |
| 2 | Site-to-Site VPN Connection | Delete the VPN connection |
| 3 | Virtual Private Gateway | Detach from VPC, then delete |
| 4 | Customer Gateway | Delete the customer gateway |
| 5 | VPCs | Delete both VPCs (subnets, route tables, IGW will be deleted automatically) |

### Detailed Cleanup Steps:

1. **Terminate EC2 Instances:**
   - EC2 Console → Instances → Select instances → Actions → Terminate

2. **Delete Site-to-Site VPN Connection:**
   - VPC Console → Site-to-Site VPN Connections → Delete

3. **Delete Virtual Private Gateway:**
   - VPC Console → Virtual Private Gateways → Detach from VPC → Delete

4. **Delete Customer Gateway:**
   - VPC Console → Customer Gateways → Delete

5. **Delete VPCs:**
   - VPC Console → Your VPCs → Delete VPC (deletes associated resources)

---

## Summary

| Step | Action |
|------|--------|
| 1 | Create On-Premise VPC (172.16.0.0/16) |
| 2 | Create AWS Cloud VPC (10.0.0.0/16) |
| 3 | Create Public Instance in On-Premise VPC |
| 4 | Create Private Instance in AWS Cloud VPC |
| 5 | Create Customer Gateway (on-premise VPN device) |
| 6 | Create Virtual Private Gateway (AWS VPN endpoint) |
| 7 | Create Site-to-Site VPN Connection |
| 8 | Download StrongSwan configuration |
| 9 | Configure StrongSwan on public instance |
| 10 | Update route tables |
| 11 | Test connectivity |

---

**Author:** Darshan Raja  
**Last Updated:** March 2026
