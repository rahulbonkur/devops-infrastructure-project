🏗️ Enterprise DevOps Infrastructure Automation Platform

Production-Ready CI/CD on AWS using Terraform, Jenkins, Ansible & Docker

⸻

📘 Executive Summary

This project implements a production-style DevOps automation platform on AWS, designed to provision infrastructure, configure systems, and deploy applications end-to-end with zero manual intervention.

The solution follows industry best practices such as:
	•	Infrastructure as Code (IaC)
	•	Immutable deployments
	•	Separation of concerns
	•	CI/CD pipeline orchestration
	•	Configuration management
	•	Secure access control

Two independent workloads are deployed on separate EC2 instances, simulating a real-world multi-tier architecture.

⸻

🎯 Business Problem Statement

Modern organizations require:
	•	Faster deployments
	•	Reliable infrastructure provisioning
	•	Repeatable environments
	•	Reduced human error
	•	Clear separation between application layers

Manual server setup and deployments lead to:
	•	Configuration drift
	•	Inconsistent environments
	•	Downtime risks

👉 This project solves those challenges using automation-first DevOps design.

⸻

🧠 Solution Overview

The platform automates:
	1.	AWS infrastructure provisioning
	2.	Server configuration
	3.	Application deployment
	4.	Verification & validation

All controlled via a single Jenkins pipeline, ensuring consistency and auditability.

⸻

🏛️ Architecture Overview

Logical Architecture

Developer
   |
   |  (Git Push)
   v
GitHub Repository
   |
   |  (Webhook / Poll SCM)
   v
Jenkins CI/CD Server
   |
   |-----------------------------
   |                             |
Terraform                        Ansible
(IaC Layer)                      (Config Layer)
   |                             |
AWS Infrastructure               EC2 Configuration
   |                             |
Docker Host EC2             Ansible Slave EC2
(Frontend App)              (Backend App)

🧭 Detailed Architecture Explanation

1️⃣ Jenkins CI/CD Controller

Role: Central automation engine

Responsibilities:
	•	Source code retrieval
	•	Infrastructure lifecycle management
	•	Configuration orchestration
	•	Deployment validation

Why Jenkins?
	•	Mature CI/CD ecosystem
	•	Declarative pipelines
	•	Easy integration with Terraform & Ansible
	•	Industry-wide adoption

⸻

2️⃣ Infrastructure Layer – Terraform

Terraform is used to provision:
	•	VPC (isolated networking)
	•	Public subnet
	•	Internet Gateway
	•	Route tables
	•	Security Groups
	•	EC2 Instances:
	•	Docker Host
	•	Ansible Slave

Key Design Decisions
	•	Remote S3 backend for state management
	•	Idempotent execution
	•	Output variables used dynamically by Ansible
	•	Infrastructure reproducibility

Terraform ensures the same environment can be recreated anytime with a single command.

⸻

3️⃣ Configuration Layer – Ansible

Ansible handles post-provisioning configuration:
	•	Package installation
	•	Docker setup
	•	Python environment configuration
	•	Application deployment
	•	Service startup

Why Ansible?
	•	Agentless architecture
	•	SSH-based execution
	•	YAML-driven playbooks
	•	Ideal for server configuration

Dynamic inventory is generated automatically using Terraform outputs, eliminating hardcoded IPs.

⸻

4️⃣ Application Deployment Strategy

🔹 Docker Host EC2 (Frontend)
	•	Runs a Dockerized portfolio website
	•	Uses:
	•	Docker
	•	Nginx inside container
	•	Exposed via port 80

Why Docker here?
	•	Container isolation
	•	Faster deployments
	•	Consistent runtime

⸻

🔹 Ansible Slave EC2 (Backend)
	•	Hosts a Python Flask application
	•	Uses:
	•	Flask
	•	Gunicorn
	•	Exposed via port 5000

Why non-containerized here?
	•	Demonstrates flexibility
	•	Shows understanding of multiple deployment strategies
	•	Mimics legacy backend services in enterprises


🔄 CI/CD Pipeline Breakdown

Stage                   | Description
------------------------|-----------------------------------------------
Workspace Cleanup       | Ensures a clean Jenkins workspace before build
Git Clone               | Fetches the latest source code from GitHub
Terraform Init          | Initializes Terraform backend and providers
Terraform Apply         | Provisions AWS infrastructure (EC2, SG, VPC)
Output Extraction       | Retrieves EC2 public IPs from Terraform outputs
Inventory Generation   | Dynamically creates Ansible inventory file
SSH Validation          | Verifies SSH connectivity to EC2 instances
Docker App Deployment  | Deploys Dockerized frontend on Docker Host EC2
Python App Deployment  | Deploys Flask backend on Ansible Slave EC2
Health Checks          | Validates application availability via HTTP
Deployment Summary     | Displays final application URLs



  📂 Repository Structure (Industry Standard)

  .
├── ansible/
│   ├── deploy_docker_app.yml
│   ├── deploy_python_app.yml
│   └── inventory_template.ini
│
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│
├── portfolio-website/
│   ├── Dockerfile
│   └── index.html
│
├── recipe-app/
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
│       └── index.html
│
├── jenkins/
│   └── Jenkinsfile
│
├── README.md
└── .gitignore

🔐 Security Considerations
	•	SSH key-based authentication
	•	Least-privilege IAM policies
	•	No credentials hardcoded
	•	Security groups restrict ports
	•	Jenkins secrets stored securely
	•	Terraform state encrypted in S3

⸻

📊 Deployment Validation

Successful deployment provides:
	•	Frontend Application
  http://<docker_host_public_ip>

  •	Backend Application
  http://<ansible_slave_public_ip>:5000

Health checks are performed automatically via Ansible and Jenkins.
📈 Engineering Best Practices Applied
	•	Infrastructure as Code
	•	Idempotent deployments
	•	Stateless builds
	•	Modular automation
	•	Separation of concerns
	•	Reproducible environments
	•	Zero manual configuration

⸻

🧪 Testing & Validation Strategy
	•	Port availability checks
	•	HTTP status validation
	•	Process verification
	•	Deployment logs review

⸻

🎤 Interview-Ready Explanation (Golden Line)

“I designed and implemented a fully automated DevOps platform on AWS using Terraform for infrastructure provisioning, Jenkins for CI/CD orchestration, and Ansible for configuration management, deploying both containerized and backend applications across isolated EC2 environments.”

⸻

🚀 Future Enhancements (Enterprise Roadmap)
	•	Application Load Balancer
	•	Auto Scaling Groups
	•	ECS / Kubernetes migration
	•	Secrets Manager integration
	•	Centralized logging (ELK)
	•	Monitoring with Prometheus & Grafana
	•	Blue/Green deployments

⸻

👨‍💻 Author

Rahul Bonkur
Junior DevOps Engineer
AWS • CI/CD • Docker • Terraform • Ansible
  
