import os
from dotenv import load_dotenv

load_dotenv()

# Configuration
class Config:
    EMBEDDING_MODEL = "text-embedding-3-small"  # OpenAI
    # EMBEDDING_MODEL = "sentence-transformers/all-mpnet-base-v2"  # HuggingFace
    LLM_MODEL = "gpt-3.5-turbo"  # or "meta-llama/Llama-2-7b-chat-hf"
    
    # Paths
    DATA_DIR = "data"
    VECTOR_STORE_PATH = "vector_store"
    VECTOR_STORE = "faiss"  # or "chroma"
    
    # Document Processing
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 200
    
    # API Keys
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Ensure required directories exist
os.makedirs(Config.DATA_DIR, exist_ok=True)
os.makedirs(Config.VECTOR_STORE_PATH, exist_ok=True)
