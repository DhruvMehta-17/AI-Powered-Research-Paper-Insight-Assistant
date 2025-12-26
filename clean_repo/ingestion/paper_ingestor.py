import uuid
from ingestion.pdf_loader import extract_text_with_pages



class Paper:
    def __init__(self, paper_id, pages):
        self.paper_id = paper_id
        self.pages = pages
        self.full_text = "\n".join(p["text"] for p in pages)
        self.sections = []  # optional later

from ingestion.pdf_loader import extract_text_with_pages


def ingest_paper(pdf_path: str):
    return extract_text_with_pages(pdf_path)



