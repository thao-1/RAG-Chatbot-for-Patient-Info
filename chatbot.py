from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOpenAI
from langchain_community.llms import HuggingFaceHub
from vector_store import load_vector_store
from config import Config

class MedicalChatbot:
    def __init__(self):
        self.vector_store = load_vector_store()
        self.llm = self._get_llm()
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vector_store.as_retriever(
                search_kwargs={"k": 4}
            ),
            return_source_documents=True
        )

    def _get_llm(self):
        if Config.LLM_MODEL.startswith("gpt"):
            return ChatOpenAI(
                model_name=Config.LLM_MODEL,
                temperature=0.3,
                openai_api_key=Config.OPENAI_API_KEY
            )
        else:
            return HuggingFaceHub(
                repo_id=Config.LLM_MODEL,
                huggingfacehub_api_token=Config.HF_TOKEN,
                model_kwargs={"temperature": 0.3}
            )

    def ask(self, question):
        result = self.qa_chain({"query": question})
        answer = result["result"]
        sources = list(set(
            doc.metadata["source"] for doc in result["source_documents"]
        ))
        return {
            "answer": answer,
            "sources": sources
        }