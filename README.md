<<<<<<< HEAD
# DevOps Infrastructure Project

Complete DevOps infrastructure with Terraform, Jenkins, Docker, and Ansible.

## 📁 Repository Structure
devops-infrastructure-project/
├── portfolio-website/          # UI/UX Portfolio (Docker)
│   ├── index.html
│   └── Dockerfile
├── recipe-app/                 # Food Recipe App (Python Flask)
│   ├── app.py
│   ├


── templates/
│   │   └── index.html
│   └── requirements.txt
├── terraform/                  # Infrastructure as Code
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
├── ansible/                    # Configuration Management
│   ├── inventory_template.ini
│   ├── deploy_docker_app.yml
│   └── deploy_python_app.yml
├── jenkins/                    # CI/CD Pipeline
│   └── Jenkinsfile
└── README.md## 🚀 Features

- **UI/UX Portfolio**: Professional portfolio with animations
- **Recipe App**: Indian food recipes for bachelors
- **Terraform**: AWS VPC, EC2, Security Groups
- **Docker**: Containerized web application
- **Ansible**: Automated configuration management
- **Jenkins**: Complete CI/CD pipeline

## 📋 Prerequisites

- AWS Account
- Jenkins Server
- Terraform installed
- Ansible installed
- SSH Key Pair (devops-key)

## 🔧 Setup Instructions

1. Clone this repository
2. Update `YOUR_USERNAME` in Ansible playbooks
3. Configure AWS credentials
4. Upload SSH key to Jenkins
5. Create Jenkins pipeline using Jenkinsfile
6. Run pipeline

## 🌐 Access Applications

- Portfolio: `http://<DOCKER_HOST_IP>`
- Recipe App: `http://<ANSIBLE_SLAVE_IP>:5000`

## 📝 License

MIT License
=======
# devops-infrastructure-project
>>>>>>> 7a0c0ba5c045826303d95734f30b226fbe5c6164
