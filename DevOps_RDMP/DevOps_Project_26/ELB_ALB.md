# Scalable Web Application Infrastructure Using AWS ASG & ALB
![alt text](<EBL project.png>)
## Project Overview

In this project, I designed and implemented a **highly available and scalable web application infrastructure on AWS** using **Auto Scaling Groups (ASG)** and an **Application Load Balancer (ALB)**.

The primary goal of this project is to automatically handle fluctuating traffic by scaling compute resources up and down while ensuring **high availability**, **fault tolerance**, and **cost optimization**.

This project reflects a real-world cloud architecture commonly used in production environments.

---

## Architecture Components Explanation

### EC2 (Elastic Compute Cloud)
**What it is:**  
Amazon EC2 provides resizable virtual servers in the cloud.

**How it is used:**  
EC2 instances host the web application (e.g., Nginx / backend service).

**Why it is used:**  
It offers flexible compute capacity and integrates seamlessly with Auto Scaling and Load Balancers.

---

### AMI (Amazon Machine Image)
**What it is:**  
A pre-configured image containing OS, application, and dependencies.

**How it is used:**  
The AMI is referenced by the Launch Template to create identical EC2 instances.

**Why it is used:**  
Ensures consistency and faster provisioning during scaling events.

---

### Launch Template
**What it is:**  
A blueprint that defines EC2 instance configuration.

**How it is used:**  
The Auto Scaling Group uses the Launch Template to launch instances.

**Why it is used:**  
Standardizes instance creation (AMI, instance type, security group, user data).

---

### Auto Scaling Group (ASG)
**What it is:**  
A service that automatically adjusts the number of EC2 instances.

**How it is used:**  
Maintains minimum, desired, and maximum EC2 instance counts.

**Why it is used:**  
Ensures high availability during peak traffic and reduces cost during low traffic.

---

### Application Load Balancer (ALB)
**What it is:**  
A Layer 7 load balancer that distributes HTTP/HTTPS traffic.

**How it is used:**  
Routes incoming traffic to EC2 instances via a Target Group.

**Why it is used:**  
Provides fault tolerance, health checks, and intelligent routing.

---

### Target Group
**What it is:**  
A logical group of EC2 instances registered with the Load Balancer.

**How it is used:**  
ALB forwards requests to healthy instances in the Target Group.

**Why it is used:**  
Decouples load balancer from EC2 instances and supports health checks.

---

### CloudWatch & Scaling Policies
**What it is:**  
AWS monitoring and alerting service.

**How it is used:**  
Monitors metrics such as CPU utilization or request count.

**Why it is used:**  
Triggers automatic scaling actions based on demand.

---

## Traffic Flow

1. User sends a request.
2. DNS (Route 53) resolves the domain.
3. Request reaches the Application Load Balancer.
4. ALB forwards traffic to the Target Group.
5. Target Group routes requests to EC2 instances in the ASG.
6. Application processes the request and returns a response.

---

## Auto Scaling Workflow

1. CloudWatch monitors application metrics.
2. Scaling policy evaluates thresholds.
3. Auto Scaling Group launches or terminates EC2 instances.
4. New instances register with the Target Group.
5. Load Balancer routes traffic only to healthy instances.

---

## AWS Resource Creation & Deletion Order

### Creation Order
1. AMI  
2. Launch Template  
3. Target Group  
4. Load Balancer  
5. Auto Scaling Group  

### Deletion Order
1. Auto Scaling Group  
2. Target Group  
3. Load Balancer  
4. Launch Template  
5. AMI / Snapshot  

---

## Interview Questions & Answers

### Why did you use Auto Scaling Group?
Auto Scaling Group ensures that the application automatically scales based on traffic demand, maintaining availability and optimizing costs.

---

### What is the role of the Launch Template?
The Launch Template defines how EC2 instances are launched, including AMI, instance type, security groups, and user data.

---

### Why Application Load Balancer instead of Network Load Balancer?
ALB operates at Layer 7, supports HTTP/HTTPS traffic, and provides advanced routing and health checks suitable for web applications.

---

### How does Auto Scaling know when to scale?
Auto Scaling uses CloudWatch metrics like CPU utilization or request count and triggers scaling policies when thresholds are crossed.

---

### What happens if an EC2 instance becomes unhealthy?
The Load Balancer stops routing traffic to it, and the Auto Scaling Group replaces it with a healthy instance.

---

## Key Learnings From This Project

- Designed a **scalable and highly available AWS architecture**
- Hands-on experience with **ASG, ALB, Launch Templates, and AMIs**
- Implemented **automatic scaling using CloudWatch**
- Understood **real-world AWS resource dependencies**
- Learned **production-level infrastructure design principles**

---

## One-Line Project Summary

> Built a scalable AWS infrastructure using Auto Scaling Groups and Application Load Balancer to ensure high availability, fault tolerance, and cost efficiency.

---
