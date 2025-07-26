# Express T2S App - Version 2 (Beginner Friendly)

## Purpose

This version introduces how to containerize a Node.js + Express web application, build a Docker image, and push it to Amazon Elastic Container Registry (ECR) using various tools. It also explains the automation scripts used, line by line, so that even someone with no prior experience can follow.

---

## What You Will Learn

- What Docker, AWS CLI, and Terraform are
- How to build and push Docker images to AWS
- How to use Python and Bash scripts for automation
- How to use Terraform to provision AWS infrastructure

---

## Step-by-Step Breakdown

### 1. Dockerfile

This file tells Docker how to build your app.

```
FROM node:18
WORKDIR /app
COPY . .
RUN npm install
CMD ["node", "index.js"]
```

- `FROM node:18` → Use Node.js version 18 as the base image
- `WORKDIR /app` → Create a working directory inside the container
- `COPY . .` → Copy all local files to the container
- `RUN npm install` → Install project dependencies
- `CMD ["node", "index.js"]` → Start the server

---

### 2. Python Script (push_to_ecr.py)

```python
import boto3
import subprocess

repo_name = "t2s-express-app"
region = "us-east-1"
image_tag = "latest"

ecr = boto3.client('ecr', region_name=region)
sts = boto3.client('sts')
account_id = sts.get_caller_identity()["Account"]
repo_uri = f"{account_id}.dkr.ecr.{region}.amazonaws.com/{repo_name}"

try:
    ecr.describe_repositories(repositoryNames=[repo_name])
except ecr.exceptions.RepositoryNotFoundException:
    ecr.create_repository(repositoryName=repo_name)

subprocess.run(f"aws ecr get-login-password --region {region} | docker login --username AWS --password-stdin {repo_uri}", shell=True, check=True)
subprocess.run(f"docker build -t {repo_name} .", shell=True, check=True)
subprocess.run(f"docker tag {repo_name}:{image_tag} {repo_uri}:{image_tag}", shell=True, check=True)
subprocess.run(f"docker push {repo_uri}:{image_tag}", shell=True, check=True)
```

- Uses AWS SDK (`boto3`) to connect to AWS
- Gets the account ID
- Checks if the ECR repo exists; if not, creates it
- Logs in to ECR
- Builds Docker image
- Tags the image for ECR
- Pushes image to ECR

---

### 3. Bash Script (push_to_ecr.sh)

```bash
#!/bin/bash
REPO_NAME=t2s-express-app
REGION=us-east-1
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
IMAGE_TAG=latest

aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com

aws ecr describe-repositories --repository-names $REPO_NAME --region $REGION > /dev/null 2>&1
if [ $? -ne 0 ]; then
  aws ecr create-repository --repository-name $REPO_NAME --region $REGION
fi

docker build -t $REPO_NAME .
docker tag $REPO_NAME:$IMAGE_TAG $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$REPO_NAME:$IMAGE_TAG
docker push $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$REPO_NAME:$IMAGE_TAG
```

Same as Python script, but written in Bash for Linux/macOS terminal users.

---

### 4. Terraform Script

```hcl
provider "aws" {
  region = var.region
}

resource "aws_ecr_repository" "app" {
  name = var.repo_name
}

resource "null_resource" "docker_push" {
  provisioner "local-exec" {
    command = <<EOT
      aws ecr get-login-password --region ${var.region} | docker login --username AWS --password-stdin ${var.account_id}.dkr.ecr.${var.region}.amazonaws.com
      docker build -t ${var.repo_name} ..
      docker tag ${var.repo_name}:latest ${var.account_id}.dkr.ecr.${var.region}.amazonaws.com/${var.repo_name}:latest
      docker push ${var.account_id}.dkr.ecr.${var.region}.amazonaws.com/${var.repo_name}:latest
    EOT
  }
}
```

- Uses the AWS provider
- Creates an ECR repo
- Pushes Docker image to ECR using shell commands

---

### 5. Terraform Variables

```hcl
variable "region" {
  description = "The region where you host your repo"
}

variable "repo_name" {
  description = "The name you want to give to the repo"
}

variable "account_id" {
  description = "Your AWS account ID"
}
```

---

## Tools Explained

- **Docker**: Packages your app into containers that run the same everywhere
- **AWS CLI**: Command-line tool to interact with AWS
- **boto3**: Python SDK for AWS
- **Terraform**: Infrastructure as Code tool to define AWS resources
- **GitHub Actions**: Automates build and deployment pipelines

---

## Next Step

After mastering this version, continue to **Version 3** to:
- Automate everything using GitHub Actions CI/CD
- Deploy to AWS ECS Fargate with full pipeline

---

## Author

**Dr. Emmanuel Naweji, 2025**  
Cloud | DevOps | SRE | FinOps | AI Engineer  
GitHub: [Here2ServeU](https://github.com/Here2ServeU)
