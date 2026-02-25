from opensearchpy import OpenSearch
from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv("OPENSEARCH_HOST")
USERNAME = os.getenv("OPENSEARCH_USERNAME")
PASSWORD = os.getenv("OPENSEARCH_PASSWORD")

def get_client():
    client = OpenSearch(
        hosts=[{'host': HOST, 'port': 443}],
        http_auth=(USERNAME, PASSWORD),
        use_ssl=True,
        verify_certs=True
    )
    return client
