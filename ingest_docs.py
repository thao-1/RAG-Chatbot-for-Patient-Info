import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("ingest.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import (
    DirectoryLoader,
    PyPDFLoader,
    CSVLoader,
    UnstructuredHTMLLoader
)
from vector_store import get_vector_store
from config import Config
import os

def load_documents():
    # Add specific loader for drugs database
    drugs_csv_path = os.path.join(Config.DATA_DIR, "drugsComTest_raw.csv")
    
    loaders = [
        DirectoryLoader(Config.DATA_DIR, glob="**/*.pdf", loader_cls=PyPDFLoader),
        DirectoryLoader(Config.DATA_DIR, glob="**/*.html", loader_cls=UnstructuredHTMLLoader)
    ]
    
    documents = []
    # First try to load the drugs database specifically
    if os.path.exists(drugs_csv_path):
        try:
            # Example of customizing CSV loader if needed
            csv_loader = CSVLoader(
                file_path=drugs_csv_path,
                csv_args={
                    'delimiter': ',',
                    'quotechar': '"'
                },
                source_column="drugName",  # Adjust to match your CSV structure
                content_columns=["condition", "review", "rating"]  # Adjust to match your CSV structure
            )
            documents.extend(csv_loader.load())
            print(f"Loaded drugs database: {drugs_csv_path}")
        except Exception as e:
            print(f"Error loading drugs database: {e}")
    
    # Then load other documents
    for loader in loaders:
        try:
            documents.extend(loader.load())
        except Exception as e:
            print(f"Error loading documents: {e}")
    
    return documents

def process_documents():
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=Config.CHUNK_SIZE,
        chunk_overlap=Config.CHUNK_OVERLAP
    )
    
    documents = load_documents()
    chunks = text_splitter.split_documents(documents)
    
    # Add metadata sources
    for chunk in chunks:
        if not chunk.metadata.get("source"):
            chunk.metadata["source"] = "unknown"
    
    return chunks

def build_vector_store():
    try:
        chunks = process_documents()
        if not chunks:
            print("Warning: No documents were processed. Vector store will be empty.")
            return
            
        vector_store = get_vector_store(chunks)
        print(f"Vector store created with {len(chunks)} chunks")
    except Exception as e:
        print(f"Error building vector store: {e}")

if __name__ == "__main__":
    build_vector_store()
