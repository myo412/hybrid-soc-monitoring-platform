from opensearchpy import OpenSearch
import json

# Your OpenSearch endpoint
host = "https://search-soc-opensearch-qsrjupnbire6cj7gzsddsrqijq.aos.us-east-1.on.aws"
auth = ('soc_admin', 'Mohits8939@')  # basic auth

client = OpenSearch(
    hosts=[host],
    http_auth=auth,
    use_ssl=True,
    verify_certs=False
)

# Load CloudTrail JSON
with open("cloudtrail_test.json", "r") as f:
    data = json.load(f)

# Handle Records key if exists
events = data.get("Records", [data])

# Push each event to OpenSearch
for event in events:
    client.index(index="soc-logs", body=event)

print("Upload complete!")
