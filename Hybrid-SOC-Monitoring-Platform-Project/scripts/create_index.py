from config.config import get_client

client = get_client()

index_name = "soc-logs"

if not client.indices.exists(index=index_name):
    client.indices.create(index=index_name)
    print("Index created successfully.")
else:
    print("Index already exists.")
