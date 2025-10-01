# CI Demo 🚀

This repository demonstrates a **basic CI/CD pipeline** using **GitHub Actions**.
It includes:

* ✅ **Python app** (`app.py`) with a simple function
* ✅ **Unit tests** (`test_app.py`) using `pytest`
* ✅ **CI workflow** to run tests on every push/PR
* ✅ **Build and push Docker image** to GitHub Container Registry (or Docker Hub)
* ✅ **Upload test results** as an artifact for inspection

---

## 📂 Repo Structure

```
ci-demo/
├── app.py               # Simple Python app
├── test_app.py          # Unit tests
├── requirements.txt     # Runtime dependencies (optional)
├── Dockerfile           # Build app container
└── .github/
    └── workflows/
        └── ci.yml       # GitHub Actions pipeline
```

---

## ⚡ How the Pipeline Works

1. **Trigger**: Runs on every `push` to `main` and on Pull Requests.
2. **Test Job**:

   * Checks out code
   * Sets up Python
   * Installs test dependencies
   * Runs `pytest` and uploads results (`pytest.xml`) as artifact
3. **Build & Push Job**:

   * Runs only if tests succeed
   * Builds Docker image from `Dockerfile`
   * Pushes image to **GitHub Container Registry** (GHCR) or **Docker Hub**
   * Tags image with both `latest` and commit SHA

---

## 🔧 Local Development

Run app locally:

```bash
python app.py
# Output: 5
```

Run tests locally:

```bash
pip install pytest
pytest
```

Build & run Docker image:

```bash
docker build -t ci-demo:local .
docker run --rm ci-demo:local
# Output: 5
```

---

## 🐳 Docker Image Tags

* `latest` → Always points to the latest successful build from `main`
* `<commit-sha>` → Immutable image linked to a specific commit

---

## 🔐 Registry Setup

### GitHub Container Registry (GHCR)

* Workflow uses built-in `GITHUB_TOKEN` (with `packages: write` permission).
* Image is pushed to:

  ```
  ghcr.io/<your-username>/ci-demo:latest
  ```

### Docker Hub (optional)

1. Generate a **Docker Hub Access Token**.
2. Add repo secrets:

   * `DOCKERHUB_USERNAME`
   * `DOCKERHUB_TOKEN`
3. Update `ci.yml` to use Docker Hub login action.

---

## 📦 Artifacts

After every run, the test report (`pytest-report`) is uploaded.
You can download it from the **Actions → Workflow run → Artifacts** section.

---

## 🚀 Next Steps

* Add caching for dependencies to speed up builds.
* Add automated security scans for Docker image.
* Extend pipeline for deployment (staging → production).

---
