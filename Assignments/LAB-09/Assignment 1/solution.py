SOURCES = {
    "S1": {"claim": "Hallucinations fell by 35% in a legal-summary benchmark.", "domain": "legal summaries"},
    "S4": {"claim": "No measurable reduction appeared in a small clinical QA evaluation.", "domain": "clinical QA"},
}

def compare(left, right):
    direct = left["claim"].startswith("Hallucinations fell") and right["claim"].startswith("No measurable reduction")
    return {"relationship": "genuine conflict" if direct else "gap",
            "reason": "The sources evaluate different domains and datasets, so their results may not be comparable."}

def synthesize():
    result = compare(SOURCES["S1"], SOURCES["S4"])
    result["summary"] = f"S1 reports a reduction; S4 reports none. {result['reason']}"
    return result

if __name__ == "__main__":
    print(synthesize())

