import sys
import os

# ✅ Add project root to PYTHONPATH
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

import streamlit as st

#from backend.indexing.faiss_index import FAISSIndex
#from backend.llm.groq_client import GroqLLM
#from backend.rag.qa_pipeline import QAPipeline

from indexing.faiss_index import FAISSIndex
from llm.groq_client import GroqLLM
from rag.qa_pipeline import QAPipeline


st.set_page_config(page_title="Research Intelligence System", layout="wide")

st.title("📚 Research Intelligence System")
st.caption("RAG-based Question Answering with Source Verification")


@st.cache_resource
def load_pipeline():
    index = FAISSIndex()
    index.load("faiss_store")

    llm = GroqLLM()
    qa = QAPipeline(index, llm)
    return qa


qa_pipeline = load_pipeline()

question = st.text_input(
    "Ask a question",
    placeholder="e.g. What is the rational use of medicines?"
)

if st.button("Ask") and question.strip():
    with st.spinner("Thinking..."):
        result = qa_pipeline.ask(question)

    st.subheader("✅ Answer")
    st.write(result["answer"])

    st.subheader("📚 Sources")
    st.text(result["sources"])
