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
- Conda (Miniconda or Anaconda)
- Git
- OpenAI API Key (place in `.env` file)

## 3. Create and activate conda environment
```bash
conda create -n webrag python=3.11
conda activate webrag

```
# Web RAG Chatbot
A web-based knowledge QA chatbot built with Python.
Input any website URL, crawl webpage content, split text, generate embeddings, store vectors in FAISS, and answer questions based on the crawled webpage content.

## ✨ Features
- Crawl web page content from input URL using BeautifulSoup
- Text chunking and embedding generation
- Local vector storage with FAISS
- Retrieval-Augmented Generation(RAG) question answering
- Simple web UI powered by Gradio
- Source citation for retrieved documents (source page return for RAG traceability)

## 🛠 Tech Stack
- Python 3.11
- LangChain
- BeautifulSoup4 (Web Crawler)
- FAISS (Vector Database)
- Gradio (Web Frontend)
- OpenAI Embeddings / LLM

## 📋 Prerequisites
- Conda (Miniconda or Anaconda)
- Git
- OpenAI API Key (place in `.env` file)

## 3. Create and activate conda environment
```bash
conda create -n webrag python=3.11
conda activate webrag
```

🚀 Installation
Install all dependencies:

```
pip install -r requirements.txt
```

▶ Run locally

```
python main.py
```

Open browser and visit: `http://127.0.0.1:7860`

## 📁 Project Structure

```
web-rag-chatbot/
├── main.py              # Gradio frontend entry
├── rag_pipeline.py      # Core RAG logic
├── requirements.txt     # Python dependencies
├── .env                 # API keys (NOT committed to git)
├── .gitignore           # Git ignore rules
└── README.md
```

## ⚙ Environment Configuration

Create a `.env` file in project root directory and fill your API key:

```
OPENAI_API_KEY=your_api_key_here
```

## ⚠ Notes & Limitations

1. This crawler works best for static HTML pages; pages rendered by JavaScript may not extract content correctly.
2. Respect website `robots.txt` before crawling any site.
3. **Never commit `.env` file or API secrets to GitHub.**
4. FAISS index files will be generated locally, excluded from git by `.gitignore`.

## 📄 License

MIT
