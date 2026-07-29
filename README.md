# 📚 Course RAG Assistant

An AI-powered Retrieval-Augmented Generation (RAG) application that answers questions directly from university course materials.

## Features

- PDF document ingestion
- Text preprocessing
- Semantic chunking
- FAISS vector database
- SentenceTransformer embeddings
- Google Gemini LLM
- Streamlit web interface
- Multi-course support
  - Differential Equations
  - Digital Logic
  - Physics

## Tech Stack

- Python
- LangChain
- FAISS
- HuggingFace Embeddings
- Google Gemini API
- Streamlit

## Run

```bash
pip install -r requirements.txt
python vector_store.py
streamlit run app.py
