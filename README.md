CI/CD Pipeline: Multi-Environment Deployment (Dev → Staging → Prod)

This project demonstrates a complete CI/CD pipeline using GitHub Actions, Docker, and a Linux VM as a deployment target.
It covers automated testing, image building, multi-environment deployment, approval gates, Slack notifications, and secrets management.

🧱 Pipeline Stages
Stage	Purpose	Description
Test	Continuous Integration	Runs automated unit tests using pytest and uploads reports.
Build	Build & Publish	Builds Docker image and pushes it to GitHub Container Registry (GHCR).
Deploy to Dev	Continuous Delivery	Automatically deploys the built image to a dev environment (port 5000).
Deploy to Staging	QA/Pre-Production	Deploys the same image to staging environment (port 5001) for testing.
Deploy to Prod	Production Deployment	Deploys to production environment (port 80) with manual approval gate.
Notify	Slack Notification	Sends a Slack message after successful production deployment.
🧩 Technologies Used

GitHub Actions – CI/CD automation

Docker – Containerization

GHCR (GitHub Container Registry) – Image hosting

Slack Webhook – Deployment notifications

SSH – Secure remote deployments

Python + Pytest – Example application and test framework

⚙️ Environment Setup
1. Create GitHub Environments

Go to:
Settings → Environments → New Environment

Create:

dev

staging

production

2. Add Secrets to Each Environment
Secret Name	Description
SSH_PRIVATE_KEY	Private SSH key to connect to VM
SERVER_IP	Target server’s IP address
SERVER_USER	Server username (e.g., ubuntu, root)
SLACK_WEBHOOK_URL	Slack incoming webhook URL (for notifications)

For production, set Required Reviewers → adds a manual approval gate.

🧾 Workflow Overview (.github/workflows/ci.yml)

The pipeline runs automatically when code is pushed to:

main

develop

release/* branches.

Job Flow

test → build → deploy-dev → deploy-staging → deploy-prod → notify

Production job requires manual approval before running.

🌍 Accessing Deployed Environments
Environment	URL Example	Port
Dev	http://<SERVER_IP>:5000	5000
Staging	http://<SERVER_IP>:5001	5001
Prod	http://<SERVER_IP>	80

Check running containers:

ssh <SERVER_USER>@<SERVER_IP>
docker ps


View logs:

docker logs ci-demo-prod

🧠 Key Learnings

End-to-end automation using GitHub Actions.

Multi-environment pipelines with approval gates.

Secure secret management through GitHub Environments.

Continuous feedback via Slack notifications.

Practical container deployment to remote VM.
