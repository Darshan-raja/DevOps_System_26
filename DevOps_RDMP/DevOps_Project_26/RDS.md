RDC with private instace

1 Steps to create VPC and subnet
    --> Number of Availability Zones (AZs) (2)
    --> Number of public subnets (2)
    --> Number of private subnets (2)
    --> NAT gateways ($) - updated (zonal why  ) , (in 1 AZ)
    --> Internet gateway (IGW) (1)
    --> Route table (1)
    --> Network connections (3)
2 Steps to create RDS Private instance and Public insta ce
    --> Application and OS Images (Amazon Machine Image) (ubunt)

3. Steps to create RDS (create Subnets grops)
   --> VPC (create)
   --> Subent (1 aveli, Private & 2nd pivate)
4. Steps to create Database
   --> Choose a database creation method (Full configuration)
   --> Choose a database engine (MySQL)
   --> Choose a database version (8.0.26)
   --> Choose a database instance class (db.t2.micro)
   --> Choose a database instance identifier (devopsdb)
   --> Choose a master username (devops)
   --> Choose a master password (devops123)
   --> Choose a database name (devopsdb)
Storage type (gp3)
Compute resource (Connect to an EC2 compute resource)
EC2 instance    (Select an EC2 private instance)

DB subnet group(Choose existing)

conntect prirvate instance to RDS
mysql -h <RDS-endpoint> -P 3306 -u <username> -p



to delete RDS
1. Delete the RDS instance
2. Delete the EC2 instance
3. Delete the DB subnet group
4. Delete the VPC