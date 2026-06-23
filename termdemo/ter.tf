# ============================================
# PART 1: TERRAFORM CONFIGURATION
# ============================================

# Specify the required providers and their versions
# terraform {
#   required_providers {
#     aws = {
#       source  = "hashicorp/aws"  # Official AWS provider from HashiCorp
#       version = "~> 5.0"         # Use version 5.x (automatically gets latest 5.x)
#     }
#   }
# }

# Configure the AWS Provider with default region
# provider "aws" {
#   region = "us-east-1"  # Change this to your preferred AWS region
#   # Note: Credentials are picked from environment variables or ~/.aws/credentials
# }

# ============================================
# PART 2: CREATE IAM USER
# ============================================

# Resource: aws_iam_user
# Purpose: Creates a new IAM user in AWS account
# IAM = Identity and Access Management - manages users, groups, and permissions
resource "aws_iam_user" "ec2_operator" {  # Name of the resource "aws_iam_user" is ak  "ec2_operator"
  # The actual username that will be created in AWS
  # Must be unique within the AWS account
  name = "EC2-permission-user"
  
  # Optional: Add tags to identify this user
  tags = {
    Environment = "DevOps_Lab"
    CreatedBy   = "Terraform"
    Purpose     = "EC2 Management"
  }
}

# ============================================
# PART 3: CREATE CUSTOM IAM POLICY
# ============================================

# Resource: aws_iam_policy
# Purpose: Creates a custom policy defining what actions are allowed/denied
# This policy follows the Principle of Least Privilege (only give needed permissions)
resource "aws_iam_policy" "ec2_policy" {
  # Name of the policy (visible in AWS Console)
  name        = "EC2_Management_Policy"
  
  # Optional: Description to explain what this policy does
  description = "Allows starting, stopping, and describing EC2 instances"
  
  # The policy document in JSON format
  # jsonencode() converts Terraform code to valid JSON
  policy = jsonencode({
    # AWS policy version (current version is 2012-10-17)
    Version = "2012-10-17"
    
    # Statement array - contains one or more permission statements
    Statement = [
      {
        # Effect: Can be "Allow" or "Deny"
        # "Allow" gives permissions, "Deny" explicitly blocks them
        Effect = "Allow"
        
        # Action: List of AWS API calls that are allowed
        # Format: <service>:<action>
        # Here, we allow 4 specific EC2 actions
        Action = [
          "ec2:StartInstances",        # Start a stopped EC2 instance
          "ec2:StopInstances",         # Stop a running EC2 instance
          "ec2:DescribeInstances",     # List/view EC2 instances
          "ec2:DescribeInstanceStatus" # Check status of EC2 instances
        ]
        
        # Resource: Which resources this applies to
        # "*" means ALL EC2 instances in the account
        # For better security, you can restrict to specific instances
        Resource = "*"
      }
    ]
  })
  
  # Tags for the policy
  tags = {
    Environment = "DevOps_Lab"
    CreatedBy   = "Terraform"
  }
}

# ============================================
# PART 4: ATTACH POLICY TO USER
# ============================================

# Resource: aws_iam_user_policy_attachment
# Purpose: Attaches the custom policy to the IAM user
# This is what actually gives the user 
resource "aws_iam_user_policy_attachment" "attach_policy" {
  # Reference to the user we created earlierACA
  # aws_iam_user.ec2_operator.name gets the name attribute from the user resource
  user = aws_iam_user.ec2_operator.name
  
  # Reference to the policy we created earlier
  # aws_iam_policy.ec2_policy.arn gets the ARN (Amazon Resource Name) of the policy
  # ARN is a unique identifier for AWS resources
  policy_arn = aws_iam_policy.ec2_policy.arn
}

# ============================================
# PART 5: CREATE AN EC2 INSTANCE
# ============================================

# Resource: aws_instance
# Purpose: Launches a virtual server (EC2 instance) in AWS
# EC2 = Elastic Compute Cloud - AWS's virtual machine service
resource "aws_instance" "iam_instance" {
  # AMI: Amazon Machine Image - the operating system template
  # This is like a snapshot of an OS with specific configurations
  # To find the right AMI, go to: AWS Console → EC2 → Launch Instance → Copy AMI ID
  # Note: AMI IDs are region-specific! This one is for us-east-1
  ami = "ami-0bc7aabcf58d1e02a"  # Amazon Linux 2 (free tier eligible)
  
  # Instance Type: Determines the hardware (CPU, memory, etc.)
  # t3.micro is in the AWS Free Tier (1 vCPU, 1 GB RAM)
  # Other options: t2.micro, t3.small, t3.medium, etc.
  instance_type = "t3.micro"
  
  # Key Pair: Used for SSH access to the instance
  # This must already exist in AWS (create in EC2 Console → Key Pairs)
  # Replace with your actual key pair name
  key_name = "new version1.1"  # ⚠️ WARNING: Spaces in key names can cause issues!
  
  # Security Groups: Firewall rules (not specified here, uses default)
  # For production, always specify a security group
  
  # User Data: Script to run when instance starts (optional)
  # Uncomment to add a startup script
  # user_data = <<-EOF
  #   #!/bin/bash
  #   echo "Hello from EC2!" > /var/www/html/index.html
  #   systemctl start httpd
  #   EOF
  
  # Tags: Labels to organize and identify resources
  tags = {
    Name        = "EC2-Terraform-Instance"  # Display name in AWS Console
    Environment = "DevOps_Lab"
    CreatedBy   = "Terraform"
    Purpose     = "Demo for IAM User Practice"
  }
  
  # Volume Tags: Tags for the root volume (disk)
  volume_tags = {
    Name        = "EC2-Root-"
    Environment = "DevOps_Lab"
  }
}

# ============================================
# PART 6: OUTPUTS (Information to display)
# ============================================

# Output: Displays useful information after terraform apply
# These values will be shown in the terminal

# Display the IAM user ARN
output "iam_user_arn" {
  description = "ARN of the created IAM user"
  value       = aws_iam_user.ec2_operator.arn
}

# Display the policy ARN
output "iam_policy_arn" {
  description = "ARN of the created IAM policy"
  value       = aws_iam_policy.ec2_policy.arn
}

# Display the EC2 instance ID
output "ec2_instance_id" {
  description = "ID of the EC2 instance"
  value       = aws_instance.iam_instance.id
}

# Display the EC2 instance public IP
output "ec2_public_ip" {
  description = "Public IP of the EC2 instance"
  value       = aws_instance.iam_instance.public_ip
}

# Display the EC2 instance public DNS
output "ec2_public_dns" {
  description = "Public DNS of the EC2 instance"
  value       = aws_instance.iam_instance.public_dns
}

# ============================================
# PART 7: ADDITIONAL SECURITY GROUP (OPTIONAL)
# ============================================

# Resource: aws_security_group
# Purpose: Firewall rules to control traffic to the EC2 instance
# This is OPTIONAL - uncomment if you want to add it

# resource "aws_security_group" "ec2_sg" {
#   name        = "ec2-terraform-sg"
#   description = "Allow SSH and HTTP traffic"
#   
#   # Inbound Rules (what can access the instance)
#   ingress {
#     description = "SSH from anywhere"
#     from_port   = 22
#     to_port     = 22
#     protocol    = "tcp"
#     cidr_blocks = ["0.0.0.0/0"]  # ⚠️ Allow SSH from anywhere (not secure for production)
#   }
#   
#   ingress {
#     description = "HTTP from anywhere"
#     from_port   = 80
#     to_port     = 80
#     protocol    = "tcp"
#     cidr_blocks = ["0.0.0.0/0"]
#   }
#   
#   # Outbound Rules (what the instance can access)
#   egress {
#     from_port   = 0
#     to_port     = 0
#     protocol    = "-1"  # All protocols
#     cidr_blocks = ["0.0.0.0/0"]
#   }
#   
#   tags = {
#     Name        = "EC2-Terraform-SG"
#     Environment = "DevOps_Lab"
#   }
# }

# To use the security group, add this to the aws_instance resource:
# vpc_security_group_ids = [aws_security_group.ec2_sg.id]

# ============================================
# PART 8: VARIABLES (For reusability)
# ============================================

# Variable: Allows you to customize the configuration
# Instead of hardcoding values, use variables

# variable "instance_type" {
#   description = "EC2 instance type"
#   type        = string
#   default     = "t3.micro"
# }
# 
# variable "ami_id" {
#   description = "AMI ID for the EC2 instance"
#   type        = string
#   default     = "ami-0bc7aabcf58d1e02a"
# }
# 
# variable "key_name" {
#   description = "Key pair name for SSH access"
#   type        = string
#   default     = "my-key-pair"
# }

# Then use them like:
# instance_type = var.instance_type
# ami           = var.ami_id
# key_name      = var.key_name