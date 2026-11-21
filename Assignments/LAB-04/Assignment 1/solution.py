MEMORY = {
    "database": ["Decision: use PostgreSQL for production storage."],
    "hosting": ["Decision: deploy the frontend on the campus VM."],
}

def retrieve(topic, query):
    if topic not in MEMORY:
        return []
    return [record for record in MEMORY[topic]
            if any(word in record.lower() for word in query.lower().split())]

if __name__ == "__main__":
    for topic, query in [("database", "database production"), ("hosting", "hosting frontend")]:
        records = retrieve(topic, query)
        print(f"{topic} answer: {records}")
    assert "hosting" not in " ".join(retrieve("database", "database production")).lower()
    assert "database" not in " ".join(retrieve("hosting", "hosting frontend")).lower()

