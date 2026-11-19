ROWS = [
    {"event": "AI Club Talk", "category": "technical", "signups": 12},
    {"event": "Robotics Demo", "category": "technical", "signups": 18},
    {"event": "Career Panel", "category": "social", "signups": 9},
]

def answer():
    trace = [{"tool": "read_csv", "rows": ROWS}]
    filtered = [row for row in ROWS if row["category"] == "technical"]
    trace.append({"step": "filter", "category": "technical", "rows": filtered})
    if not filtered:
        raise ValueError("No technical events; average not computed.")
    values = [row["signups"] for row in filtered]
    average = sum(values) / len(values)
    trace.append({"tool": "calculator", "values": values, "average": average})
    return average, trace

if __name__ == "__main__":
    average, trace = answer()
    print(f"Technical event average: {average:.1f}")
    for entry in trace:
        print(entry)

