from rag.prompt_builder import build_prompt


class QAPipeline:
    def __init__(self, faiss_index, llm):
        self.index = faiss_index
        self.llm = llm

    def ask(self, question):
        retrieved = self.index.search(question, top_k=5)

        prompt = build_prompt(question, retrieved)
        answer = self.llm.generate(prompt)

        return {
            "answer": answer,
            "sources": self.format_sources(retrieved)
        }

        # -------- NEW FEATURE: SUMMARY -------- #
    def get_summary(self):
        chunks = self.index.get_top_chunks(k=5) if hasattr(self.index, "get_top_chunks") else []
        context = "\n".join([c["text"] if isinstance(c, dict) else str(c) for c in chunks])

        prompt = (
            "Provide a short structured academic summary of this research paper:\n"
            "- Problem Statement\n- Method / Approach\n- Key Contributions\n- Results / Findings\n"
            "Keep it factual and concise.\n\n"
            f"Context:\n{context}"
        )

        return self.llm.generate(prompt)

    # -------- NEW FEATURE: KEYWORDS -------- #
    def get_keywords(self):
        chunks = self.index.get_top_chunks(k=5) if hasattr(self.index, "get_top_chunks") else []
        context = "\n".join([c['text'] if isinstance(c, dict) else str(c) for c in chunks])

        prompt = (
            "Extract 5–7 important technical keywords from this paper. "
            "Return them as a simple comma-separated list.\n\n"
            f"Context:\n{context}"
        )

        return self.llm.generate(prompt)


    def format_sources(self, sources):
        lines = []
        for i, s in enumerate(sources, 1):
            lines.append(
                f"[{i}] Section: {s.get('section', 'N/A')} | "
                f"Page: {s.get('page_start', 'N/A')} | "
                f"Chunk ID: {s.get('chunk_id', 'N/A')}"
            )
        return "\n".join(lines)
