🔷 Architecture Summary
VPC-1
•	CIDR: 10.0.0.0/24
•	Public Subnet: 10.0.0.0/28
•	Private Subnet: 10.0.0.64/27
•	Internet Gateway attached
•	Public + Private Route Tables
VPC-2
•	CIDR: 10.0.1.0/26
•	Private Subnet: 10.0.1.0/27
•	Private Route Table only
Then:
•	Create VPC Peering
•	Update routes
•	Configure Security Groups
•	Launch EC2 and test connectivity
________________________________________
🌐 Final Target Architecture
 
 
 
 
________________________________________
🔷 PHASE 1 – Create VPC-1
Step 1: Open VPC Service
1.	Login to AWS Console
2.	Search → VPC
3.	Click Create VPC
________________________________________
Step 2: Create VPC-1
Choose:
✔ VPC only
Fill:
Name: VPC-1
IPv4 CIDR: 10.0.0.0/24
Tenancy: Default
Click Create VPC
________________________________________
🔷 PHASE 2 – Create Subnets in VPC-1
Go to:
VPC → Subnets → Create Subnet
________________________________________
Step 3: Create Public Subnet
VPC: VPC-1
Name: VPC1-Public-Subnet
CIDR: 10.0.0.0/28
Availability Zone: Any (example ap-south-1a)
Create.
________________________________________
Step 4: Create Private Subnet
VPC: VPC-1
Name: VPC1-Private-Subnet
CIDR: 10.0.0.64/27
AZ: Same or different
Create.
________________________________________
🔷 PHASE 3 – Configure Internet for VPC-1
Step 5: Create Internet Gateway
Go to:
VPC → Internet Gateways → Create
Name: IGW-VPC1
Create.
________________________________________
Step 6: Attach Internet Gateway
1.	Select IGW-VPC1
2.	Click Attach to VPC
3.	Select VPC-1
4.	Attach
________________________________________
🔷 PHASE 4 – Configure Route Tables (VPC-1)
________________________________________
Step 7: Create Public Route Table
VPC → Route Tables → Create
Name: VPC1-Public-RT
VPC: VPC-1
Create.
________________________________________
Step 8: Add Internet Route
1.	Select VPC1-Public-RT
2.	Go to Routes
3.	Click Edit Routes
4.	Add:
Destination: 0.0.0.0/0
Target: Internet Gateway (IGW-VPC1)
Save.
________________________________________
Step 9: Associate Public Subnet
1.	Go to Subnet Associations
2.	Click Edit
3.	Select VPC1-Public-Subnet
4.	Save
________________________________________
Step 10: Create Private Route Table (VPC-1)
Name: VPC1-Private-RT
VPC: VPC-1
Create.
________________________________________
Step 11: Associate Private Subnet
Edit Subnet Associations:
✔ Select VPC1-Private-Subnet
✔ Save
(No internet route added here)
________________________________________
🔷 PHASE 5 – Create VPC-2
________________________________________
Step 12: Create VPC-2
Name: VPC-2
CIDR: 10.0.1.0/26
Create.
________________________________________
🔷 PHASE 6 – Create Subnet in VPC-2
________________________________________
Step 13: Create Private Subnet
Name: VPC2-Private-Subnet
VPC: VPC-2
CIDR: 10.0.1.0/27
Create.
________________________________________
🔷 PHASE 7 – Create Route Table (VPC-2)
________________________________________
Step 14: Create Route Table
Name: VPC2-Private-RT
VPC: VPC-2
Create.
________________________________________
Step 15: Associate Subnet
Edit Subnet Associations:
✔ Select VPC2-Private-Subnet
✔ Save
(No internet route required)
________________________________________
🔷 PHASE 8 – Create VPC Peering Connection
________________________________________
Step 16: Create Peering
VPC → Peering Connections → Create
Name: VPC1-VPC2-Peering
Requester VPC: VPC-1
Accepter VPC: VPC-2
Region: Same region
Create.
________________________________________
Step 17: Accept Peering
Select peering connection → Actions → Accept
Status becomes Active
________________________________________
🔷 PHASE 9 – Update Route Tables for Peering
________________________________________
Step 18: Update VPC1-Private-RT
Add route:
Destination: 10.0.1.0/26
Target: Peering Connection
Save.
________________________________________
Step 19: Update VPC2-Private-RT
Add route:
Destination: 10.0.0.0/24
Target: Peering Connection
Save.
________________________________________
🔷 PHASE 10 – Launch EC2 Instances
________________________________________
Step 20: Launch Public EC2 (VPC-1 Public)
•	VPC: VPC-1
•	Subnet: VPC1-Public-Subnet
•	Enable Auto-assign Public IP
•	Security Group:
o	Allow SSH (22) from 0.0.0.0/0
Launch.
________________________________________
Step 21: Launch Private EC2 (VPC-1 Private)
•	VPC: VPC-1
•	Subnet: VPC1-Private-Subnet
•	No public IP
•	Security Group:
o	Allow SSH from 10.0.0.0/24
Launch.
________________________________________
Step 22: Launch Private EC2 (VPC-2)
•	VPC: VPC-2
•	Subnet: VPC2-Private-Subnet
•	No public IP
•	Security Group:
o	Allow SSH from 10.0.0.64/27
Launch.
________________________________________
🔷 PHASE 11 – Test Connectivity
________________________________________
Step 23: SSH to Public EC2
From your laptop:
ssh -i key.pem ec2-user@Public-IP
________________________________________
Step 24: From Public → SSH into VPC1 Private
ssh ec2-user@10.0.0.X
________________________________________
Step 25: From VPC1 Private → SSH into VPC2 Private
ssh ec2-user@10.0.1.X
