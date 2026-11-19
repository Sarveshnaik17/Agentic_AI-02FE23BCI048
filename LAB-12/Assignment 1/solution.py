BUDGET_LIMIT = 500

def authorize(proposal, finance_approved=False):
    if "estimated_cost" not in proposal or proposal["estimated_cost"] is None:
        return {"status": "rejected", "reason": "Cost estimate is required."}
    if proposal["estimated_cost"] > BUDGET_LIMIT and not finance_approved:
        return {"status": "rejected", "reason": "Budget limit exceeded without finance approval."}
    return {"status": "approved"}

if __name__ == "__main__":
    cases = [
        ({"action": "scale service", "estimated_cost": 400}, False),
        ({"action": "buy servers"}, False),
        ({"action": "buy servers", "estimated_cost": 900}, False),
        ({"action": "buy servers", "estimated_cost": 900}, True),
    ]
    for proposal, finance_ok in cases:
        print(proposal, authorize(proposal, finance_ok))

