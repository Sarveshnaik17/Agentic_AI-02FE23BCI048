class GovernedAgent:
    def __init__(self):
        self.since_evaluation = 0
        self.evaluations = 0

    def evaluate(self):
        self.evaluations += 1
        self.since_evaluation = 0
        return {"status": "evaluated", "count": self.evaluations}

    def propose(self, proposal):
        if self.since_evaluation >= 5:
            return {"status": "blocked", "message": "Re-evaluation required before another proposal."}
        self.since_evaluation += 1
        return {"status": "accepted", "proposal": proposal}

if __name__ == "__main__":
    agent = GovernedAgent()
    agent.evaluate()
    for number in range(1, 7):
        print(number, agent.propose(f"proposal-{number}"))
    print(agent.evaluate())
    print("After re-evaluation:", agent.propose("proposal-6"))

