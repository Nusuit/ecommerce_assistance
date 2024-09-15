from ..rag.retriever import Retriever
from ..rag.generator import Generator
from ..recommendation.engine import RecommendationEngine
from .history import DialogHistory

class DialogManager:
    def __init__(self, retriever: Retriever, generator: Generator, rec_engine: RecommendationEngine):
        self.retriever = retriever
        self.generator = generator
        self.rec_engine = rec_engine
        self.history = DialogHistory("user123")  # In a real app, you'd manage multiple users

    def process_input(self, user_input: str) -> str:
        retrieved_docs = self.retriever.retrieve(user_input)
        response = self.generator.generate(user_input, retrieved_docs)
        
        self.history.add_interaction(user_input, response)
        
        # Check if we should add a recommendation
        if self._should_recommend():
            recommendation = self.rec_engine.get_recommendation(self.history.analyze_preferences())
            response += f"\n\nYou might also be interested in: {recommendation}"
        
        return response

    def _should_recommend(self) -> bool:
        # Simple logic: recommend every 3 interactions
        return len(self.history.history) % 3 == 0