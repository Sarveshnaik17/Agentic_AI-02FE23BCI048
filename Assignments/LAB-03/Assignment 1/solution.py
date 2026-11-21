article = {
    "title": "Campus learning platform pilot",
    "claims": [
        {"claim": "Hosting cost fell by 40%.", "evidence": "one department estimate", "sample_size": 1},
        {"claim": "Quiz accuracy improved by 12%.", "evidence": "controlled study of 800 students", "sample_size": 800},
    ],
}

def apply_research_summary_skill(source):
    selected = max(source["claims"], key=lambda item: item["sample_size"])
    return {"source": source["title"], "main_claim": selected["claim"],
            "evidence": selected["evidence"],
            "selection_note": "Two unrelated claims were present; the better-supported claim was selected."}

if __name__ == "__main__":
    print(apply_research_summary_skill(article))

