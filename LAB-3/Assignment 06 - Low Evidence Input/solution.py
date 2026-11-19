article = {"title": "Study app", "text": "The new study app improves focus for students."}

def summarize(source):
    text = source["text"].lower()
    evidence = "not stated in source"
    limitation = "not stated in source"
    if "study of" in text or "surveyed" in text or "participants" in text:
        evidence = "Evidence details are described in the source."
    if "limitation" in text or "however" in text:
        limitation = "A limitation is described in the source."
    return {"claim": source["text"], "evidence": evidence, "limitation": limitation}

if __name__ == "__main__":
    result = summarize(article)
    print(result)
    assert result["evidence"] == "not stated in source"
    assert result["limitation"] == "not stated in source"
    print("No unsupported evidence or limitation was added.")

