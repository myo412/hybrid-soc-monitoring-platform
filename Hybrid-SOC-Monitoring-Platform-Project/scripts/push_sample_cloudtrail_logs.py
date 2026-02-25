# push_sample_cloudtrail_logs_opensearch.py
import random
from datetime import datetime, timedelta
from opensearchpy import OpenSearch

# -----------------------------
# Configure OpenSearch
# -----------------------------
host = "search-soc-opensearch-qsrjupnbire6cj7gzsddsrqijq.aos.us-east-1.on.aws"
port = 443

auth = ("soc_admin", "Mohits8939@")  # OpenSearch master user

client = OpenSearch(
    hosts=[{"host": host, "port": port}],
    http_auth=auth,
    use_ssl=True,
    verify_certs=True,   # set False if you want to ignore TLS errors (not recommended)
    connection_class=None
)

# -----------------------------
# Generate sample logs
# -----------------------------
NUM_EVENTS = 120
USERS = ["alice", "bob", "charlie", "dave", "eve"]
EVENTS = ["ConsoleLogin", "CreateUser", "DeleteBucket", "UpdateBucketPolicy", "PutObject"]
IP_BASE = "192.168.1."

for i in range(NUM_EVENTS):
    record = {
        "eventName": random.choice(EVENTS),
        "userName": random.choice(USERS),
        "sourceIPAddress": f"{IP_BASE}{random.randint(1,50)}",
        "eventTime": (datetime.now() - timedelta(minutes=random.randint(0,1200))).isoformat()
    }
    client.index(index="soc-logs", body=record)  # note: use 'body=' here

print(f"{NUM_EVENTS} sample CloudTrail logs pushed!")
