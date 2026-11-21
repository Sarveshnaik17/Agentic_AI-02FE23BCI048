BUDGET_CAP = 1100

def critique(proposal):
    total = sum(item["cost"] for item in proposal.values())
    log = []
    if total > BUDGET_CAP:
        excess = total - BUDGET_CAP
        log.append({"conflict": "overall budget cap", "total": total, "cap": BUDGET_CAP,
                    "rule": "budget_over_preference"})
        proposal["marketing"]["cost"] = max(0, proposal["marketing"]["cost"] - excess)
        log.append({"resolution": "reduced optional marketing spend", "cut": excess})
    return proposal, log

if __name__ == "__main__":
    draft = {"venue": {"cost": 600}, "food": {"cost": 300},
             "activity": {"cost": 150}, "marketing": {"cost": 200, "plan": "campus posters"}}
    print("Roles: logistics, food, activity, marketing")
    result, log = critique(draft)
    print("Conflict log:", log)
    print("Final costs:", result)
    assert sum(item["cost"] for item in result.values()) <= BUDGET_CAP

