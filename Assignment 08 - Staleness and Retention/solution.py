from datetime import date

TODAY = date(2026, 11, 17)
RETENTION_DAYS = 30
RECORDS = {
    "fresh": {"decision": "Keep weekly backups.", "date": date(2026, 11, 15)},
    "old": {"decision": "Use the legacy mail host.", "date": date(2026, 8, 1)},
}

def answer(record):
    age = (TODAY - record["date"]).days
    warning = None
    if age > RETENTION_DAYS:
        warning = f"This decision is from {age} days ago and may be out of date."
        return {"warning": warning, "decision": None}
    return {"warning": warning, "decision": record["decision"]}

if __name__ == "__main__":
    for label in ("fresh", "old"):
        print(label, answer(RECORDS[label]))
    assert answer(RECORDS["fresh"])["warning"] is None
    assert answer(RECORDS["old"])["warning"] is not None
    assert answer(RECORDS["old"])["decision"] is None

