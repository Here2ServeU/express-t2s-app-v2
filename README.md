# Express T2S Web App – Beginner-Friendly DevOps Project

## Overview

Welcome! This project walks you step-by-step through deploying a web app using real-world DevOps tools, even if you have no technical background.

You'll learn to:
- Build and run a Node.js + Express web app
- Containerize it with Docker
- Push it to AWS using Bash, Python, and Terraform
- Understand what each file and command does along the way

---

## What's Inside This Project?

| File/Folder | Purpose |
|-------------|---------|
| `index.js` | Main application code that runs the web server |
| `public/index.html` | A simple form for users to sign up |
| `.gitignore` | Tells Git what to exclude (like secret files or system clutter) |
| `Dockerfile` | Instructions to turn the app into a Docker container |
| `scripts/bash_deploy_to_ecr.sh` | A script to automate AWS ECR deployment using Bash |
| `scripts/deploy_to_ecr.py` | The same deployment automated using Python |
| `terraform/` | Contains files to automate cloud infrastructure setup |
| `README.md` | This guide! |

---

## Step-by-Step Setup

### 1. Clone the Project

```bash
git clone https://github.com/Here2ServeU/express-t2s-app-v2.git
cd express-t2s-app-v2
```

---

### 2. Install Node.js (If not already installed)

Download it from [https://nodejs.org](https://nodejs.org)  
Then run:

```bash
npm install
node index.js
```

Now visit: `http://localhost:3000` in your browser.

---

## Understand Each File (Line by Line)

### `index.js`

```js
const express = require('express');           // Loads Express
const app = express();                        // Initializes the app
const path = require('path');                 // Helps find folder paths

app.use(express.static('public'));            // Tells Express to serve files from /public

app.use(express.urlencoded({ extended: true }));  // Helps process form data

app.post('/signup', (req, res) => {
  const { fullName, email, interests } = req.body;
  console.log('Signup received:', fullName, email, interests);
  res.send('Thank you for signing up!');
});

app.listen(3000, () => console.log('App is running on http://localhost:3000'));
```

---

### `.gitignore`

```txt
node_modules/       # Exclude Node.js libraries
.env                # Don't upload secret environment variables
.vscode/            # Ignore local editor settings
logs
*.log
terraform/
*.tfstate*
```

---

### `Dockerfile`

```dockerfile
FROM node:18                        # Use official Node 18 image
WORKDIR /app                        # Set working directory inside the container
COPY . .                            # Copy everything into /app
RUN npm install                     # Install dependencies
EXPOSE 3000                         # Open port 3000 for the app
CMD ["node", "index.js"]            # Start the app
```

---

### `scripts/bash_deploy_to_ecr.sh`

```bash
#!/bin/bash
REPO_NAME="express-t2s-ecr"
AWS_REGION="us-east-1"
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)

# Login to AWS ECR
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com

# Create repo if not exist
aws ecr describe-repositories --repository-names $REPO_NAME || aws ecr create-repository --repository-name $REPO_NAME

# Build & Push
docker build -t $REPO_NAME .
docker tag $REPO_NAME:latest $ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$REPO_NAME
docker push $ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$REPO_NAME
```

---

### `scripts/deploy_to_ecr.py`

```python
import subprocess

# Replace with your info
repo = "express-t2s-ecr"
region = "us-east-1"

def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

account_id = subprocess.getoutput("aws sts get-caller-identity --query Account --output text")
login_cmd = f"aws ecr get-login-password --region {region} | docker login --username AWS --password-stdin {account_id}.dkr.ecr.{region}.amazonaws.com"
run(login_cmd)

# Build, tag, push
run(f"docker build -t {repo} .")
run(f"docker tag {repo}:latest {account_id}.dkr.ecr.{region}.amazonaws.com/{repo}")
run(f"docker push {account_id}.dkr.ecr.{region}.amazonaws.com/{repo}")
```

---

### Terraform

#### `main.tf`

```hcl
provider "aws" {
  region = var.aws_region
}

resource "aws_ecr_repository" "app" {
  name = var.repo_name
}
```

#### `variables.tf`

```hcl
variable "aws_region" {
  default = "us-east-1"
}

variable "repo_name" {
  default = "express-t2s-ecr"
}
```

#### `terraform.tfvars`

```hcl
aws_region = "us-east-1"
repo_name  = "express-t2s-ecr"
```

Run:

```bash
cd terraform
terraform init
terraform apply
```

---

## Final Project Structure

```
express-t2s-app-v2/
├── public/index.html
├── index.js
├── Dockerfile
├── .gitignore
├── scripts/
│   ├── bash_deploy_to_ecr.sh
│   └── deploy_to_ecr.py
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   └── terraform.tfvars
├── README.md
```

---

## About the Author

**Dr. Emmanuel Naweji**  
Cloud | DevOps | SRE | FinOps | AI  
Helping engineers and organizations build real, scalable infrastructure.

- [LinkedIn](https://linkedin.com/in/ready2assist/)
- [GitHub](https://github.com/Here2ServeU)

© 2025 Emmanuel Naweji. All rights reserved.

