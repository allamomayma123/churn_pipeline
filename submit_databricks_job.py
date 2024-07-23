import requests
import json

def submit_databricks_job():
    url = "https://adb-3733434531606738.18.azuredatabricks.net/api/2.1/jobs/runs/submit"  # Added API endpoint
    headers = {
        "Authorization": f"Bearer dapifb38d2ec392f9618738a14757d23e556-3",
        "Content-Type": "application/json"
    }
    payload = {
        "run_name": "EDA job",
        "existing_cluster_id": "0723-084144-1yim17rl",
        "notebook_task": {
            "notebook_path": "/Workspace/Repos/omayma.allam@artefact.com/churn-databricks/DATA_PREPARATION"
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print(response.json())

if __name__ == "__main__":
    submit_databricks_job()
