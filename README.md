# Express T2S App - Version 2

## Purpose

This version deploys the Dockerized Express T2S web application to AWS using ECS (Elastic Container Service) with Fargate, a serverless container compute engine. It also introduces a GitHub Actions CI/CD pipeline that automatically builds the Docker image, pushes it to AWS ECR (Elastic Container Registry), and triggers deployment to ECS.

This version is ideal for those who want to learn how to automate deployment pipelines using real-world tools used in DevOps and Cloud Engineering.

---

## Features

- **GitHub Actions CI/CD pipeline** for build and deployment
- **Docker image built locally or in pipeline**
- **AWS ECR** integration for image hosting
- **AWS ECS (Fargate)** for serverless container orchestration
- **Load balancer** for handling traffic
- Environment variables managed through AWS

---

## Project Structure

```
express-t2s-app-v3/
├── .github/
│   └── workflows/
│       └── ci.yml                # GitHub Actions pipeline definition
├── Dockerfile                    # Docker build instructions
├── index.js                      # Node.js + Express server
├── package.json
└── README.md
```

---

## Prerequisites

Before deploying, ensure you have the following:

- **GitHub account** with repository created
- **AWS account** with:
  - ECR repository created
  - ECS Cluster and Fargate task role set up
  - IAM user with programmatic access
- **AWS CLI** installed and configured on your machine
- **GitHub Secrets** added:
  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`
  - `AWS_REGION`
  - `ECR_REPO_URI`

---

## How the Deployment Works (Step-by-Step)

1. **Docker Image Built**:
   The GitHub Actions workflow builds the Docker image from your `Dockerfile`.

2. **Push Image to ECR**:
   The built image is pushed to your AWS ECR repository.

3. **Trigger ECS Update**:
   The ECS task definition is updated to use the new image. ECS then replaces the running task with the new one.

---

## GitHub Actions Workflow Explained

Located at `.github/workflows/ci.yml`:

```yaml
name: Build and Deploy to ECS

on:
  push:
    branches:
      - main

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Code
      uses: actions/checkout@v3

    - name: Login to AWS ECR
      run: |
        aws configure set region ${{ secrets.AWS_REGION }}
        aws ecr get-login-password | docker login --username AWS --password-stdin ${{ secrets.ECR_REPO_URI }}

    - name: Build Docker Image
      run: docker build -t t2s-web .

    - name: Tag and Push Docker Image
      run: |
        docker tag t2s-web:latest ${{ secrets.ECR_REPO_URI }}:latest
        docker push ${{ secrets.ECR_REPO_URI }}:latest

    - name: Update ECS Service
      run: |
        aws ecs update-service --cluster t2s-cluster --service t2s-service --force-new-deployment
```

---

## Deployment Instructions (for Non-Technical Users)

### Step 1: Clone the Repository

```bash
git clone https://github.com/Here2ServeU/express-t2s-app.git
cd express-t2s-app/express-t2s-app-v3
```

### Step 2: Add Secrets to GitHub

Go to your GitHub repo → Settings → Secrets and variables → Actions → New repository secret.

Add these keys:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_REGION` (e.g., `us-east-1`)
- `ECR_REPO_URI` (e.g., `123456789.dkr.ecr.us-east-1.amazonaws.com/t2s-web`)

### Step 3: Push Changes

Once you push changes to the `main` branch, the GitHub Actions workflow is triggered automatically.

```bash
git add .
git commit -m "Test deployment to ECS"
git push origin main
```

### Step 4: Monitor Deployment

- Log in to [AWS Console](https://console.aws.amazon.com/)
- Go to ECS → Clusters → `t2s-cluster` → `t2s-service`
- Confirm task is running and attached to a load balancer

### Step 5: Visit Your App

Use the DNS name from your ECS Load Balancer to access your deployed app in the browser.

---

## Next Step

Move to **Version 4** to:
- Create an EKS (Elastic Kubernetes Service) cluster with Terraform
- Package app using Helm
- Deploy via GitOps with ArgoCD

---

## Author

**Emmanuel Naweji, 2025**  
Cloud | DevOps | SRE | FinOps | AI Engineer  
GitHub: [Here2ServeU](https://github.com/Here2ServeU)

