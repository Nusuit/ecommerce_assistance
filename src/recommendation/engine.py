import requests
from typing import Dict, List
from ..config import REC_ENGINE_URL, REC_ENGINE_API_KEY

class RecommendationEngine:
    def __init__(self):
        self.url = REC_ENGINE_URL
        self.api_key = REC_ENGINE_API_KEY

    def get_recommendations(self, user_id: str, preferences: Dict[str, Any]) -> List[str]:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        payload = {
            "user_id": user_id,
            "preferences": preferences
        }
        response = requests.post(f"{self.url}/recommend", json=payload, headers=headers)
        response.raise_for_status()
        return response.json()["recommendations"]

    def get_recommendation(self, preferences: Dict[str, Any]) -> str:
        recommendations = self.get_recommendations("anonymous", preferences)
        return recommendations[0] if recommendations else "No recommendation available"