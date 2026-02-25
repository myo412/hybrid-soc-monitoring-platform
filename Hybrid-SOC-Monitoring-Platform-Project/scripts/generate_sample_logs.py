import json
import random
from datetime import datetime

events = ["LoginSuccess", "LoginFailed", "FileAccess", "IAMChange"]

logs = []

for i in range(200):
    log = {
        "eventTime": datetime.utcnow().isoformat(),
        "eventName": random.choice(events),
        "sourceIP": f"192.168.1.{random.randint(1,255)}",
        "username": f"user{random.randint(1,10)}"
    }
    logs.append(log)

with open("../data/sample_logs.json", "w") as f:
    json.dump(logs, f, indent=4)

print("Sample logs generated.")
