<!-- what is deops -->
--> DevOps is a set of practices that combines software development (Dev) and IT operations (Ops) to streamline the process of delivering software applications It aims to improve collaboration, communication and automation between development teams and operations teams to ensure faster and more reliable software delivery.

DevOps practices include continuous integration, continuous delivery, continuous monitoring, and continuous improvement. These practices enable teams to work together more effectively, reduce the time to market, and improve the quality of software applications.

EC2 (Elastic Compute Cloud)
EC2 stands for Elastic Compute Cloud.

Resizable computing capacity means you can increase or decrease the processing power based on your workload, avoiding overpaying or lacking resources.

**EC2 stands for Amazon Elastic Compute Cloud, a core service of AWS.
**
Amazon EC2 (Elastic Compute Cloud) is a cloud service provided by AWS that allows us to create and use virtual servers on the internet.

It is used to run applications, websites, and services without buying physical servers.

--> EC2 helps to:

Avoid overload and under-utilization of servers

Increase or decrease computing power whenever needed

Pay only for the resources we use

EC2 is:

Scalable – we can increase or decrease CPU, memory, and instances

Flexible – supports different operating systems and configurations

Reliable – runs on AWS global infrastructure

Very Simple One-Line Definition (Interview)

EC2 is a service that provides virtual servers in the cloud where we can run applications and scale resources based on demand.

Example (Easy to Understand)

Traffic is low → use 1 EC2 instance

Traffic is high → add more EC2 instances

Traffic reduces → remove extra instances

This way, performance is maintained and cost is saved.

Compentens of EC2 :

what is instance is a virtual server in the cloud that we can use to run applications and services over the internet.

--> Instance types are different configurations of virtual servers that we can use to run our applications and services.

--> Instance types are categorized into different families, such as:
General purpose, Compute optimized, Memory optimized, Storage optimized,high performance Capacitive instances, and accelerated networkingBare metal instances.

--> General purpose instances are designed for general computing tasks, such as running web servers, databases, and development environments.

--> Compute optimized instances are designed for compute-intensive tasks, such as running scientific simulations and data analysis.

--> Memory optimized instances are designed for memory-intensive tasks, such as running large databases and data warehousing.

--> Storage optimized instances are designed for tasks that require high I/O performance, such as running databases and file servers.
--> High performance instances are designed for tasks that require high performance, such as running high-performance computing (HPC) applications.

--> Accelerated networking instances are designed for tasks that require high network performance, such as running machine learning and data analytics applications.

--> Bare metal instances are designed for tasks that require high performance and low latency, such as running high-performance computing (HPC) applications.

life cycle of EC2 instance
--> The life cycle of an EC2 instance is the process of creating, using, and terminating an instance.

--> The life cycle of an EC2 instance can be summarized as follows:

1. Launch: An EC2 instance is launched when you create it. You can launch an instance using the AWS Management Console, AWS CLI, or AWS SDKs.
2. Run: Once the instance is launched, it is in the running state and can be used to run applications and services. You can connect to the instance using SSH or RDP.
3. Stop: You can stop an instance when you want to pause its operation. When you stop an instance, it retains its data and configuration, but it is not billed for the time it is stopped.
4. Terminate: You can terminate an instance deletcing complete instance and all associated resources, such as volumes and snapshots.

EBS (Elastic Block Store) is a block-level storage service that provides persistent storage for EC2 instances.
AMI (Amazon Machine Image) is a template or blueprint that contains the software, operating system, and other data needed to launch an EC2 instance.
ASG (Auto sacling group) is a group of EC2 instances that are managed together. It allows you to scale out or in based on demand and also provides high availability.

types of ASG are: Horizontal Scaling, Vertical Scaling, and Load Balancing.
example is horizontal scaling is adding more instances to the group when the load increases, and vertical scaling is adding more resources to the instances when the load increases.

ELB (Elastic Load Balancer) is a service that distributes incoming application traffic across multiple targets, such as Amazon EC2 instances, containers, and IP addresses.

--> **SDLDC(software development life cycle)** is stuctured followed by development team to plan,build,test,deploy and maintain the sofware application.

>> Ther are 6 phases or stage in SDLC:

1. Planning, 2.defining/Analysis, 3. Design, 4.  building/Implementation, 5. Testing, 6. deploying/ Maintenance.

--> SDLC stands for Software Development Life Cycle.

--> SDLC is a process used by the software industry to design, develop, and test high-quality software.

--> SDLC is a series of steps or phases that a software project goes through, from initial planning to final deployment.

--> SDLC is a structured approach that helps to ensure that software is developed efficiently and effectively.

--> 




1. Planning: The first phase of SDLC involves defining the project scope, objectives, and resources required to complete the project.
2. Defining/Analysis: In this phase, the requirements of the software are gathered and analyzed to determine the functional and non-functional requirements of the software.
SRS (Software Requirements Specification) is a document that describes the requirements of the software.
A detailed Software Requirement Specification (SRS) document is created to define what needs to be built.
3. Design: In this phase, the software architecture and design are created to meet the requirements gathered in the previous phase.
   esigning Architecture
Traditional SDLC

System and software design documents are created based on requirements. This includes both high-level (HLD) and low-level design (LLD).
4. Building/Implementation: In this phase, the software is developed using the design created in the previous phase.
5. Testing: In this phase, the software is tested to ensure that it meets the requirements and is free from defects.
6. Deploying/ Maintenance: In this phase, the software is deployed to the production environment and maintained to ensure that it continues to meet the requirements and is free from defects.

For continuous integration and delivery, we use git --> jenkins --> Maven --> SonarQube --> Nexus --> Docker --> Kubernetes --> AWS

Prometheus is key part montoring tool feedback
