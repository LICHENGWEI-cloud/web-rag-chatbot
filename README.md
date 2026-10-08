# Web Knowledge Base QA Chatbot
A RAG chatbot that ingests static web pages from URL, extracts webpage content via a custom web crawler, builds a vector knowledge base, and answers questions with source citations.

## ✨ Features
- Input any static webpage URL, crawl and extract clean article content (custom BeautifulSoup scraper, not off-the-shelf loader)
- Text chunking, embedding and vector storage with FAISS local vector database
- Question answering strictly grounded on the ingested webpage context
- **Source citation support**: return original `page_content` from retrieved chunks for RAG traceability and hallucination mitigation
- Simple Gradio web UI for live interaction
- Fully local execution powered by Ollama; no OpenAI API key required for local demo

## 🛠 Tech Stack
- Python 3.11
- LangChain (LCEL)
- BeautifulSoup4 & Requests: custom web crawler
- FAISS: local vector store
- Ollama: local LLM + embedding model
- Gradio: web frontend UI

## 📋 Prerequisites
1. Install [Ollama](https://ollama.com/)
2. Pull required models from your terminal:
```bash
ollama pull nomic-embed-text
ollama pull llama3.2
3.Create and activate conda environment
```bash
conda create -n webrag python=3.11
conda activate webrag
