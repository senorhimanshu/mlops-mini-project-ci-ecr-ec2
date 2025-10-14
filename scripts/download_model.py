# scripts/download_model.py

import os
import mlflow
from mlflow.artifacts import download_artifacts

dagshub_token = os.getenv("DAGSHUB_PAT")
if not dagshub_token:
    raise EnvironmentError("DAGSHUB_PAT is required to download the model")

os.environ["MLFLOW_TRACKING_USERNAME"] = dagshub_token
os.environ["MLFLOW_TRACKING_PASSWORD"] = dagshub_token

dagshub_url = "https://dagshub.com"
repo_owner = "senorhimanshu"
repo_name = "mlops-mini-project-ci-ecr-ec2"

# Set up MLflow tracking URI
mlflow.set_tracking_uri(f'{dagshub_url}/{repo_owner}/{repo_name}.mlflow')

model_name = "my_model"
model_uri = f"models:/{model_name}/Production"

output_dir = "flask_app/models/model"
os.makedirs(output_dir, exist_ok=True)

print(f"Downloading model from {model_uri} ...")
download_artifacts(artifact_uri=model_uri, dst_path=output_dir)
print(f"✅ Model downloaded successfully to {output_dir}")

