# Medical Information Chatbot

A RAG-based chatbot that provides medical information using a vector database and language models. This project implements a Retrieval-Augmented Generation (RAG) system for medical information retrieval and question answering.

## Implementation Details

This chatbot was built using a RAG (Retrieval-Augmented Generation) architecture with the following components:

1. **Data Processing**:
   - Medical data is processed and chunked into smaller segments
   - Each chunk is embedded using OpenAI's text-embedding-3-small model
   - Chunks are stored in a FAISS vector database for efficient similarity search

2. **Retrieval System**:
   - Uses FAISS for fast and efficient similarity search
   - Retrieves the most relevant chunks based on semantic similarity
   - Configurable number of chunks (k=4) for context window

3. **Generation System**:
   - Uses GPT-3.5-turbo for answer generation
   - Combines retrieved context with the user's question
   - Generates coherent, context-aware responses
   - Includes source attribution for transparency

4. **Web Interface**:
   - Modern, responsive design using TailwindCSS
   - Real-time question answering
   - Source attribution display
   - Error handling and user feedback

## Features

- Question answering about medications, conditions, and medical information
- Source attribution for all answers
- Modern web interface
- Fast and efficient vector search using FAISS
- Support for both OpenAI and HuggingFace models

## Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd RAG-Chatbot-for-Patient-Info
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
```
Edit `.env` and add your API keys:
- `OPENAI_API_KEY`: Your OpenAI API key
- `HUGGINGFACEHUB_API_TOKEN`: (Optional) Your HuggingFace API token

5. Ingest the medical data:
```bash
python ingest_docs.py
```

## Usage

1. Start the server:
```bash
uvicorn api:app --reload
```

2. Open your browser and go to:
```
http://127.0.0.1:8000
```

3. Ask questions about:
- Medications and their side effects
- Medical conditions and symptoms
- Treatment effectiveness
- Patient experiences
- Drug interactions
- And more!

## API Endpoints

- `GET /`: Web interface
- `POST /ask`: Ask a medical question
  ```json
  {
    "question": "What are the side effects of aspirin?"
  }
  ```
- `GET /health`: Health check endpoint

## Project Structure

- `api.py`: FastAPI server implementation
- `chatbot.py`: Core chatbot logic
- `vector_store.py`: Vector database management
- `config.py`: Configuration settings
- `ingest_docs.py`: Data ingestion script
- `static/`: Web interface files

## Technologies Used

- FastAPI
- LangChain
- FAISS
- OpenAI API
- HuggingFace (optional)
- TailwindCSS

## Algorithm Details

The system uses a RAG (Retrieval-Augmented Generation) approach with the following steps:

1. **Document Processing**:
   - Documents are split into chunks using LangChain's text splitter
   - Each chunk is embedded using OpenAI's text-embedding-3-small model
   - Embeddings are stored in a FAISS vector store

2. **Query Processing**:
   - User question is converted to an embedding
   - FAISS performs similarity search to find relevant chunks
   - Retrieved chunks are used as context for the LLM

3. **Answer Generation**:
   - Context and question are combined into a prompt
   - GPT-3.5-turbo generates a response
   - Sources are tracked and returned with the answer

4. **Vector Search**:
   - FAISS (Facebook AI Similarity Search) for efficient similarity search
   - Configurable number of neighbors (k=4)
   - Cosine similarity for embedding comparison
