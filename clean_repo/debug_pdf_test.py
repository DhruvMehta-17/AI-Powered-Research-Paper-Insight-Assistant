from backend.ingestion.pdf_loader import extract_text_from_pdf

text = extract_text_from_pdf("data/standard-treatment-guidelines.pdf")

print("TEXT LENGTH:", len(text))
print("FIRST 500 CHARS:\n", text[:500])
