import boto3
import subprocess
import os
import sys

# Move to project root where Dockerfile exists
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
os.chdir(project_root)

# Configuration
repo_name = "t2s-express-app"
region = "us-east-1"
image_tag = "latest"

# Create ECR and STS clients
ecr = boto3.client('ecr', region_name=region)
sts = boto3.client('sts')

# Get AWS account ID
try:
    account_id = sts.get_caller_identity()["Account"]
except Exception as e:
    print("Error getting AWS account ID:", e)
    sys.exit(1)

# Construct full ECR repo URI
repo_uri = f"{account_id}.dkr.ecr.{region}.amazonaws.com/{repo_name}"

# Step 1: Create ECR repo if it doesn't exist
try:
    ecr.describe_repositories(repositoryNames=[repo_name])
    print(f"Repository {repo_name} already exists.")
except ecr.exceptions.RepositoryNotFoundException:
    print(f"Creating repository: {repo_name}")
    ecr.create_repository(repositoryName=repo_name)

# Step 2: Log in to ECR
print("Logging in to AWS ECR...")
subprocess.run(
    f"aws ecr get-login-password --region {region} | docker login --username AWS --password-stdin {repo_uri}",
    shell=True, check=True
)

# Step 3: Build Docker image
print("Building Docker image...")
subprocess.run(f"docker build -t {repo_name} .", shell=True, check=True)

# Step 4: Tag Docker image
print("Tagging Docker image for ECR...")
subprocess.run(f"docker tag {repo_name}:{image_tag} {repo_uri}:{image_tag}", shell=True, check=True)

# Step 5: Push image to ECR
print("Pushing image to ECR...")
subprocess.run(f"docker push {repo_uri}:{image_tag}", shell=True, check=True)

print(" Docker image successfully built, tagged, and pushed to ECR.")
