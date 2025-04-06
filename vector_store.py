from langchain_community.vectorstores import FAISS, Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
from config import Config

def get_embedding_model():
    if Config.EMBEDDING_MODEL.startswith("text-embedding"):
        return OpenAIEmbeddings(
            model=Config.EMBEDDING_MODEL,
            openai_api_key=Config.OPENAI_API_KEY
        )
    else:
        return HuggingFaceEmbeddings(
            model_name=Config.EMBEDDING_MODEL,
            model_kwargs={"device": "cpu"}
        )

def get_vector_store(chunks):
    embeddings = get_embedding_model()
    
    if Config.VECTOR_STORE == "faiss":
        vector_store = FAISS.from_documents(chunks, embeddings)
        vector_store.save_local(Config.VECTOR_STORE_PATH)
        return vector_store
    else:
        vector_store = Chroma.from_documents(
            chunks,
            embeddings,
            persist_directory=Config.VECTOR_STORE_PATH
        )
        vector_store.persist()
        return vector_store

def load_vector_store():
    embeddings = get_embedding_model()
    
    if Config.VECTOR_STORE == "faiss":
        return FAISS.load_local(
            Config.VECTOR_STORE_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )
    else:
        return Chroma(
            persist_directory=Config.VECTOR_STORE_PATH,
            embedding_function=embeddings
        )