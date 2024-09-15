import json
from datetime import datetime
from typing import List, Dict, Any
from ..recommendation.engine import RecommendationEngine

class DialogHistory:
    def __init__(self, user_id: str, max_history_length: int = 100):
        self.user_id = user_id
        self.max_history_length = max_history_length
        self.history: List[Dict[str, Any]] = []
        self.recommendation_engine = RecommendationEngine()

    def add_interaction(self, message: str, response: str, context: Dict[str, Any] = None):
        """
        Thêm một tương tác mới vào lịch sử.
        """
        interaction = {
            "timestamp": datetime.now().isoformat(),
            "message": message,
            "response": response,
            "context": context or {}
        }
        self.history.append(interaction)
        if len(self.history) > self.max_history_length:
            self.history.pop(0)

    def get_recent_interactions(self, n: int = 5) -> List[Dict[str, Any]]:
        """
        Lấy n tương tác gần đây nhất.
        """
        return self.history[-n:]

    def search_history(self, keyword: str) -> List[Dict[str, Any]]:
        """
        Tìm kiếm trong lịch sử dựa trên từ khóa.
        """
        return [
            interaction for interaction in self.history
            if keyword.lower() in interaction["message"].lower() or
            keyword.lower() in interaction["response"].lower()
        ]

    def analyze_preferences(self) -> Dict[str, Any]:
        """
        Phân tích lịch sử để xác định sở thích của người dùng.
        """
        # Đây là nơi bạn có thể thêm logic phân tích phức tạp hơn
        product_mentions = {}
        for interaction in self.history:
            # Giả sử chúng ta có một hàm extract_product_mentions
            products = self.extract_product_mentions(interaction["message"])
            for product in products:
                product_mentions[product] = product_mentions.get(product, 0) + 1
        return {"product_preferences": product_mentions}

    def get_personalized_recommendations(self) -> List[str]:
        """
        Sử dụng lịch sử để tạo đề xuất cá nhân hóa.
        """
        preferences = self.analyze_preferences()
        return self.recommendation_engine.get_recommendations(self.user_id, preferences)

    def save_to_file(self, filename: str):
        """
        Lưu lịch sử vào file.
        """
        with open(filename, 'w') as f:
            json.dump(self.history, f)

    def load_from_file(self, filename: str):
        """
        Tải lịch sử từ file.
        """
        with open(filename, 'r') as f:
            self.history = json.load(f)

    def extract_product_mentions(self, text: str) -> List[str]:
        """
        Trích xuất các đề cập đến sản phẩm từ văn bản.
        Đây là một phương thức giả định và cần được triển khai với NLP thực tế.
        """
        # Placeholder implementation
        # In a real scenario, this would use NLP techniques to extract product mentions
        return [word for word in text.split() if len(word) > 5]  # Simplistic example

# Example usage
if __name__ == "__main__":
    history = DialogHistory("user123")
    history.add_interaction("Tôi đang tìm một chiếc áo khoác màu đen.", "Chúng tôi có nhiều lựa chọn áo khoác màu đen. Bạn có preference về chất liệu không?")
    history.add_interaction("Tôi thích áo khoác da.", "Tuyệt vời! Đây là một số gợi ý về áo khoác da màu đen của chúng tôi.")
    
    print(history.get_recent_interactions())
    print(history.analyze_preferences())
    print(history.get_personalized_recommendations())