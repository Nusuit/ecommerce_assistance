import openai
from ..config import LLM_MODEL, LLM_API_KEY

class LLM:
    def __init__(self):
        openai.api_key = LLM_API_KEY
        self.model = LLM_MODEL

    def generate(self, prompt: str) -> str:
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content