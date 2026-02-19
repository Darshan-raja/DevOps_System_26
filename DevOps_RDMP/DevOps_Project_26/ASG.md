# # How to Create ASG (Auto Scaling Group) in AWS

1. **Create a VPC (Virtual Private Cloud)**
   - Resources to create (VPC and more)
   - Number of Availability Zones (AZs) (2)
   - Number of public subnets (2)
   - Number of private subnets (2)
   - NAT gateways ($) - updated (zonal), Nat gateway (in 1 AZ)
   - Internet gateway (IGW) (1)
   - Route table (1)
   - Network connections (3)

2. **Create an Instance (private one and public instance)**

3. **Create ELB (Application Load Balancer)**
   - Access for public (1)

4. **Create Target Group (2)**
   - Name given

5. **AMI (Amazon Machine Image)**
   - Launch template contents (Amazon Machine Image - select from an existing launch template)
   - Auto Scaling guidance (enable it)
   - Application and OS Images (Amazon Machine Image) - required (AMI)
   - Network settings (subnet id - don't select)

6. **ASG (Auto Scaling Group)**
   - Name
   - Launch template (tmp name)
   - Network select (VPC)
   - Availability Zones and subnets (select 4 subnets)
   - Availability Zone distribution - new (Balanced best effort)
   - Load balancing (Attach to an existing load balancer)
   - Existing load balancer target groups (existing target group)
   - Select the load balancers to attach (Choose from your load balancer target groups)
   - Automatic scaling - optional
   - Choose whether to use a target tracking policy (Target tracking scaling policy)
