from dialog.manager import DialogManager
from rag.retriever import Retriever
from rag.generator import Generator
from llm.model import LLM
from recommendation.engine import RecommendationEngine

def main():
    llm = LLM()
    retriever = Retriever()
    generator = Generator(llm)
    recommendation_engine = RecommendationEngine()
    dialog_manager = DialogManager(retriever, generator, recommendation_engine)

    while True:
        user_input = input("User: ")
        if user_input.lower() == 'exit':
            break
        response = dialog_manager.process_input(user_input)
        print(f"Assistant: {response}")

if __name__ == "__main__":
    main()