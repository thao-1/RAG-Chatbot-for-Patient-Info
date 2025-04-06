from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from chatbot import MedicalChatbot
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import traceback

app = FastAPI(
    title="Medical Chatbot API",
    description="API for querying medical information using RAG",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

class Query(BaseModel):
    question: str

chatbot = MedicalChatbot()

@app.get("/")
def root():
    return FileResponse("static/index.html")

@app.post("/ask")
def ask_question(query: Query):
    try:
        response = chatbot.ask(query.question)
        return {
            "answer": response["answer"],
            "sources": response["sources"]
        }
    except Exception as e:
        error_detail = traceback.format_exc()
        print(f"Error processing question: {error_detail}")
        raise HTTPException(
            status_code=500, 
            detail=f"Error processing your question: {str(e)}\n{error_detail}"
        )

@app.get("/health")
def health_check():
    return {"status": "healthy"}
