# CI/CD Demo with Flask, Docker, and GitHub Actions

This repository demonstrates a **CI/CD pipeline** using:
- **Flask** (Python web app)
- **Pytest** (for testing)
- **Docker** (for containerization)
- **GitHub Actions** (for CI/CD automation)
- **AWS EC2** (as a test/staging server)

---

## 🚀 App Overview

The app is a simple Flask API with two endpoints:

- `/` → returns a welcome message  
- `/add/<a>/<b>` → adds two integers and returns the result  

Example:
```bash
curl http://<YOUR_SERVER_IP>:5000
# "Hello! Your CI/CD pipeline deployed this Flask app 🚀"

curl http://<YOUR_SERVER_IP>:5000/add/5/7
# "The sum of 5 and 7 is 12"

---

📂 Project Structure
.
├── app.py              # Flask application
├── test_app.py         # Unit tests for the Flask app
├── requirements.txt    # Dependencies
├── Dockerfile          # Docker build configuration
└── .github/
    └── workflows/
        └── ci.yml      # CI/CD pipeline definition

---

**🧪 CI Pipeline**

1.Test (Pytest)

    Runs unit tests for the Flask app.

    Produces a JUnit XML report as an artifact.

2.Build & Push (Docker)

    Builds the Docker image.

    Pushes it to GitHub Container Registry (GHCR).

3.Deploy to Test Environment (EC2)

    Connects via SSH to an AWS EC2 server.

    Pulls the latest Docker image.

    Stops/removes any old container.

    Runs the new version on port 5000.

---

**⚙️ Setup Instructions**
1. AWS EC2 Setup

Launch an Ubuntu EC2 instance (free tier t2.micro is fine).

Open ports 22 (SSH) and 5000 (custom app port) in the security group.

Install Docker:

sudo apt-get update -y
sudo apt-get install docker.io -y
sudo usermod -aG docker ubuntu

2. GitHub Secrets

Add the following secrets in your repository (Settings → Secrets → Actions):

SSH_PRIVATE_KEY → private SSH key for EC2 access

TEST_SERVER_IP → EC2 public IP address

TEST_SERVER_USER → usually ubuntu

3. Run the Pipeline

Push code to main. The workflow will:

Run tests

Build and push the Docker image

Deploy to EC2

---

**🔍 Verifying Deployment**

On EC2:

docker ps


You should see a container named ci-demo running.

In your browser:

http://<YOUR_SERVER_IP>:5000
http://<YOUR_SERVER_IP>:5000/add/10/15
