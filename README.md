# 🧠 AI-Powered Research Paper Insight Assistant

*A RAG-based Research Paper Question-Answering & Insight System*

## 📌 Project Overview

The **AI-Powered Research Paper Insight Assistant** is an intelligent system that helps researchers and students:

* Upload research papers (PDFs)
* Automatically extract and index paper content
* Ask questions about the paper using **RAG (Retrieval-Augmented Generation)**
* View answers along with supporting source text
* Generate a **structured paper summary**
* Extract **important technical keywords / topics**

The project combines **FAISS vector search, LLMs, semantic chunking, and Streamlit UI** to create a practical research-assistance tool.

---

## 🏗️ System Architecture

```
PDF Upload → Ingestion → Chunking → Embeddings → FAISS Index
                          ↓
                     RAG Pipeline
                          ↓
                  LLM Answer / Summary / Keywords
                          ↓
                     Streamlit UI
```

---

## 📂 Folder Structure

```
📁 ingestion/          → PDF reading & text extraction
📁 indexing/           → chunking, embeddings, FAISS index
📁 rag/                → RAG QA pipeline + summary & keywords
📁 llm/                → LLM client implementation
📁 Frontend/app/       → Streamlit user interface
📁 uploads/            → Uploaded PDFs
```

---

## 🚀 Features

### 🔹 Core Functionality

* Upload and process research paper PDFs
* Section-wise text extraction and chunking
* FAISS-based semantic indexing
* Context-aware Question Answering (RAG)

### 🔹 Enhancements Added

* 📌 **Paper Summary generation**
* 🔎 **Key Topic / Keyword extraction**
* 🧱 Import-path cleanup and refactoring
* 🛡 Error handling for upload & chunk failures
* 🗂 Unique filename handling for uploads
* 🎨 UI improvements and custom title

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** (UI)
* **LangChain / FAISS**
* **LLM (Groq / OpenAI-compatible client)**
* **PDF processing & text extraction**

---

## ⚙️ Installation & Setup

```bash
git clone <repo-url>
cd Research-Intelligence-System

python -m venv venv
venv\Scripts\activate   # Windows
# or
source venv/bin/activate

pip install -r requirements.txt
```

Create a `.env` file and add your API key:

```
GROQ_API_KEY=your_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run Frontend/app/streamlit_app.py
```

Upload any research paper PDF and start interacting 🎯

---

## 🧪 Recommended Test PDFs
[Transformer Paper.pdf](https://github.com/user-attachments/files/24349499/Transformer.Paper.pdf)

---

## 🧠 How RAG Works in This Project

1. Extract and chunk paper text
2. Convert chunks into embeddings
3. Store them in FAISS
4. Retrieve relevant chunks based on query
5. Provide the context to the LLM
6. Generate grounded answers with sources

---

## 🔮 Future Enhancements

* Multi-paper comparison mode
* Citation graph network
* Trend analytics across research themes
* Exportable PDF insights
* Multi-document library search

---

## 👤 Author Notes

This project has been **refactored and enhanced** to improve originality and functionality, including:

* Added Paper Summary module
* Added Keyword Topic extractor
* Fixed import path restructuring
* Improved indexing stability and UI layout

---

## ⭐ Conclusion

This project demonstrates how **RAG + FAISS + LLMs + Streamlit** can be combined to build a practical and research-oriented AI assistant.

