import json
from elasticsearch import Elasticsearch

# Connect to local Elasticsearch
es = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", "quqKKCWjqtvNQN3Vgc_*"),
    verify_certs=False
)

# Load CloudTrail JSON file
with open("009889853245_CloudTrail_us-east-1_20260218T0345Z_jiYHYUFhedg7RgAN.json", "r") as f:
    data = json.load(f)

records = data["Records"]

for record in records:
    es.index(index="cloudtrail-logs", document=record)

print(f"Pushed {len(records)} records to Elasticsearch")
