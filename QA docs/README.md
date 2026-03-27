# Q&A over Custom Documents (RAG)

## 📌 Overview
This project allows you to ask questions over your own documents using LLMs and embeddings.

## ⚙️ Tech Stack
- LangChain
- FAISS
- HuggingFace Embeddings
- OpenAI LLM

## 🚀 How to Run

### 1. Install dependencies
pip install -r requirements.txt

### 2. Add documents
Put your PDF or TXT files in the `data/` folder

### 3. Process documents
python ingest.py

### 4. Run the app
python app.py

## 💡 Example Questions
- What is this document about?
- Summarize the content
- Extract key points

## 🧠 Architecture
Uses Retrieval-Augmented Generation (RAG):
- Embeddings for semantic search
- FAISS for vector storage
- LLM for answer generation