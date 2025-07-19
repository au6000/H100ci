import os
import json
import requests

LAMBDA_API_TOKEN = os.environ.get("LAMBDA_API_TOKEN")
PROJECT_ID = os.environ.get("LAMBDA_PROJECT_ID")
IMAGE_NAME = os.environ.get("LAMBDA_IMAGE_NAME", "unsloth-sft:latest")
REPO_URL = os.environ.get("LAMBDA_REPO_URL", "https://github.com/your/repo.git")

if not (LAMBDA_API_TOKEN and PROJECT_ID):
    raise SystemExit("Set LAMBDA_API_TOKEN and LAMBDA_PROJECT_ID")

endpoint = "https://cloud.lambdalabs.com/api/v1/builds"
headers = {
    "Authorization": f"Bearer {LAMBDA_API_TOKEN}",
    "Content-Type": "application/json",
}

data = {
    "project_id": PROJECT_ID,
    "image_name": IMAGE_NAME,
    "git_url": REPO_URL,
    "dockerfile_path": "Dockerfile",
}

resp = requests.post(endpoint, headers=headers, json=data)
print("Status:", resp.status_code)
try:
    print(json.dumps(resp.json(), indent=2))
except Exception:
    print(resp.text)
