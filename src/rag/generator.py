from typing import List, Dict
from ..llm.model import LLM

class Generator:
    def __init__(self, llm: LLM):
        self.llm = llm

    def generate(self, query: str, retrieved_docs: List[Dict]) -> str:
        context = "\n".join([doc["content"] for doc in retrieved_docs])
        prompt = f"Context: {context}\n\nQuestion: {query}\n\nAnswer:"
        return self.llm.generate(prompt)