from typing import List, Dict
import requests
from ..config import VECTOR_DB_URL, VECTOR_DB_API_KEY

class Retriever:
    def __init__(self):
        self.vector_db_url = VECTOR_DB_URL
        self.api_key = VECTOR_DB_API_KEY

    def retrieve(self, query: str, top_k: int = 5) -> List[Dict]:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        payload = {
            "query": query,
            "top_k": top_k
        }
        response = requests.post(f"{self.vector_db_url}/search", json=payload, headers=headers)
        response.raise_for_status()
        return response.json()["results"]