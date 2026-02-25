import json
from config.config import get_client

client = get_client()
index_name = "soc-logs"

with open("../data/sample_logs.json") as f:
    logs = json.load(f)

for record in logs:
    client.index(index=index_name, body=record)

print("Logs pushed successfully.")
