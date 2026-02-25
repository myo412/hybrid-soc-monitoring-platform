from config.config import get_client

client = get_client()

index_name = "soc-logs"

if client.indices.exists(index=index_name):
    client.indices.delete(index=index_name)
    print("Index deleted.")
else:
    print("Index does not exist.")
