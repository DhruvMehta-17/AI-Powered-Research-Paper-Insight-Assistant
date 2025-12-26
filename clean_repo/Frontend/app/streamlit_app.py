import sys
import os
import streamlit as st
import time

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../")
)
sys.path.insert(0, PROJECT_ROOT)

# from backend.ingestion.paper_ingestor import ingest_paper
# from backend.indexing.chunk_builder import build_chunks
# from backend.indexing.faiss_index import FAISSIndex
# from backend.llm.groq_client import GroqLLM
# from backend.rag.qa_pipeline import QAPipeline 

from ingestion.paper_ingestor import ingest_paper
from indexing.chunk_builder import build_chunks
from indexing.faiss_index import FAISSIndex
from llm.groq_client import GroqLLM
from rag.qa_pipeline import QAPipeline


UPLOAD_DIR = os.path.join(PROJECT_ROOT, "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

st.set_page_config(page_title="Research Intelligence System", layout="wide")
st.title("🧠 AI-Powered Research Paper Insight Assistant")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

@st.cache_resource(show_spinner=False)
def build_pipeline(pdf_path):
    paper_pages = ingest_paper(pdf_path)
    st.write("Pages Extracted:", len(paper_pages))

    chunks = build_chunks(paper_pages)
    st.write("Chunks Generated:", len(chunks))

    index = FAISSIndex()
    index.index_papers(chunks)

    llm = GroqLLM()
    return QAPipeline(index, llm)

if uploaded_file:
    #pdf_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    file_name = f"{int(time.time())}_{uploaded_file.name}"
    pdf_path = os.path.join(UPLOAD_DIR, file_name)

    #with open(pdf_path, "wb") as f:
        #f.write(uploaded_file.read())
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✅ PDF uploaded")

    with st.spinner("Indexing document..."):
        qa = build_pipeline(pdf_path)

    question = st.text_input("Ask a question")

    if question:
        result = qa.ask(question)

        st.subheader("Answer")
        st.write(result["answer"])

        st.subheader("Sources")
        st.text(result["sources"])

        st.subheader("📌 Paper Summary")
        summary = qa.get_summary()
        st.write(summary)

        with st.expander("🔎 Key Topics Found"):
            keywords = qa.get_keywords()
            st.write(keywords)
else:
    st.info("⬆️ Upload a PDF to begin")
