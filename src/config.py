import os

# Database configuration
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = os.environ.get('DB_PORT', 5432)
DB_NAME = os.environ.get('DB_NAME', 'ecommerce_assistant')
DB_USER = os.environ.get('DB_USER', 'user')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'password')

# LLM configuration
LLM_MODEL = os.environ.get('LLM_MODEL', 'gpt-3.5-turbo')
LLM_API_KEY = os.environ.get('LLM_API_KEY', 'your-api-key-here')

# RAG configuration
VECTOR_DB_URL = os.environ.get('VECTOR_DB_URL', 'http://localhost:8000')
VECTOR_DB_API_KEY = os.environ.get('VECTOR_DB_API_KEY', 'your-vector-db-api-key')

# Recommendation engine configuration
REC_ENGINE_URL = os.environ.get('REC_ENGINE_URL', 'http://localhost:8080')
REC_ENGINE_API_KEY = os.environ.get('REC_ENGINE_API_KEY', 'your-rec-engine-api-key')

# Dialog history configuration
MAX_HISTORY_LENGTH = 100