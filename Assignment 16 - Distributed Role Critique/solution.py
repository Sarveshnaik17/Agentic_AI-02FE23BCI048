DRAFT = {"total_cost": 1400, "attendees": 120, "duration_hours": 4}
ROLES = {
    "finance": lambda d: "cost exceeds 1000" if d["total_cost"] > 1000 else None,
    "venue": lambda d: "capacity exceeds 100" if d["attendees"] > 100 else None,
    "logistics": lambda d: "duration exceeds 3 hours" if d["duration_hours"] > 3 else None,
    "accessibility": lambda d: None if d["attendees"] <= 150 else "accessibility plan insufficient",
}

def distributed_critique(draft):
    objections = []
    for role, check in ROLES.items():
        objection = check(draft)
        if objection:
            objections.append({"role": role, "objection": objection})
    return objections

if __name__ == "__main__":
    result = distributed_critique(DRAFT)
    print("Independent objections:", result)
    assert len({item["role"] for item in result}) >= 2

