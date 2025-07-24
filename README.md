# Express T2S Web App – Beginner-Friendly DevOps Project

## Overview

Welcome to the Express T2S Web App project!

This project is a **beginner-friendly** guide to building and deploying a modern web application using real DevOps practices. It was designed to help individuals and organizations like **Transformed 2 Succeed (T2S)** learn how to automate deployments, run scalable infrastructure, and support real mentorship enrollment through a simple web platform.

You don’t need to be a tech expert to follow this guide. Everything is broken down in simple steps, with scripts provided for you.

---

## What This Project Does

This app lets users sign up for mentorship and sends their information to the backend. The project is structured to teach you how to:

- Build a Node.js + Express web app
- Package (containerize) it using Docker
- Push it to the cloud using AWS ECR (Elastic Container Registry)
- Deploy it using ECS (Elastic Container Service) and EKS (Elastic Kubernetes Service)
- Monitor, secure, and optimize it for reliability and cost

---

## Key Technologies

- **Node.js & Express**: Backend programming language and web framework
- **Docker**: Packages the app for cloud deployment
- **AWS (Amazon Web Services)**: Cloud platform
- **ECR**: Stores your Docker images
- **ECS & EKS**: Services for running your app on the cloud
- **Terraform**: Automates infrastructure creation

---

## Step-by-Step Setup Guide

### Step 1: Clone This Repository

First, download this project to your computer.

```bash
git clone https://github.com/Here2ServeU/express-t2s-app-v2.git
cd express-t2s-app-v2
```

---

### Step 2: Install Node.js (If Not Installed)

Go to [https://nodejs.org/](https://nodejs.org/) and download the LTS version. Install it and verify:

```bash
node -v
npm -v
```

---

### Step 3: Run the App Locally

This will install the necessary files and start the app.

```bash
npm install
node index.js
```

Visit: [http://localhost:3000](http://localhost:3000) in your browser

---

## Containerization with Docker

### What Is Docker?

Docker turns your app into a portable "container" that works anywhere—locally or in the cloud.

### Files Used

- **Dockerfile**: Instructions for Docker to build the image
- **.dockerignore**: Tells Docker what to skip (like node_modules)

---

## How to Build and Push Your App to AWS ECR

We’ve included 3 different methods so you can pick the one that suits your style.

---

### Method 1: Bash Shell Script (Easy)

File: `scripts/bash_deploy_to_ecr.sh`

Steps:
1. Log into your AWS account
2. Make the script executable:
   ```bash
   chmod +x scripts/bash_deploy_to_ecr.sh
   ```
3. Run the script:
   ```bash
   ./scripts/bash_deploy_to_ecr.sh
   ```

---

### Method 2: Python Script

File: `scripts/deploy_to_ecr.py`

Make sure Python 3 is installed. Run:

```bash
python3 scripts/deploy_to_ecr.py
```

---

### Method 3: Terraform (Automation)

Files:
- `terraform/main.tf`
- `terraform/variables.tf`
- `terraform/terraform.tfvars`

Steps:
```bash
cd terraform
terraform init
terraform apply
```

Terraform will:
- Create your ECR repo
- Set up IAM roles
- Optionally automate deployments

---

## What's in the .gitignore?

This file keeps your GitHub repo clean. It excludes:

- `node_modules/`: dependencies
- `.env`: secrets/config
- `.terraform/` & `.tfstate`: Terraform files
- System files like `.DS_Store` and `Thumbs.db`

---

## Next Phases

### ECS: Deploy to AWS Fargate
- Automatically scale app in the cloud
- Add HTTPS and domain routing

### EKS: Use Kubernetes
- Deploy using Helm charts or ArgoCD
- GitOps integration for auto-deployment

### DevSecOps:
- Scan for vulnerabilities with **Trivy**
- Use **Checkov** for Infrastructure security

### Monitoring & Cost Optimization:
- Prometheus, Grafana, CloudWatch
- Budget alerts and right-sizing

### Authentication:
- Users sign up via index.html
- Email confirmation auto-sent
- Store users in a secure database

---

## File Structure

```
express-t2s-app-v2/
├── public/
│   └── index.html
├── scripts/
│   ├── bash_deploy_to_ecr.sh
│   └── deploy_to_ecr.py
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   └── terraform.tfvars
├── Dockerfile
├── .gitignore
├── README.md
├── index.js
├── package.json
```

---

## Author

**Emmanuel Naweji**  
Cloud | DevOps | SRE | FinOps | AI Engineer  
Helping engineers, ministries, and businesses succeed through real-world DevOps

- [LinkedIn](https://www.linkedin.com/in/ready2assist/)
- [GitHub](https://github.com/Here2ServeU)
- [Medium](https://medium.com/@here2serveyou)

---

## Ready to Learn More?

Schedule a free consultation or join the mentorship program:  
👉 [https://bit.ly/letus-meet](https://bit.ly/letus-meet)

---

© 2025 Emmanuel Naweji. All rights reserved.

