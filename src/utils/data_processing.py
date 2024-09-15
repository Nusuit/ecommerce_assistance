import json
from typing import Dict, List

def load_json_file(file_path: str) -> Dict:
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json_file(data: Dict, file_path: str):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def preprocess_product_data(products: List[Dict]) -> List[Dict]:
    processed_products = []
    for product in products:
        processed_product = {
            "id": product.get("id", ""),
            "name": product.get("name", ""),
            "description": product.get("description", ""),
            "price": float(product.get("price", 0)),
            "category": product.get("category", ""),
            "tags": product.get("tags", [])
        }
        processed_products.append(processed_product)
    return processed_products

def extract_product_features(product: Dict) -> List[str]:
    features = []
    description = product.get("description", "")
    # Simple feature extraction (in reality, you'd use more sophisticated NLP techniques)
    features = [sent.strip() for sent in description.split('.') if sent.strip()]
    features.extend(product.get("tags", []))
    return list(set(features))  # Remove duplicates