class Runtime:
    def __init__(self):
        self.audit = []

    def receive_task(self, user, skill, task):
        failures = sum(entry["status"] == "error" and entry["user"] == user
                       and entry["skill"] == skill for entry in self.audit)
        if failures >= 2:
            result = {"status": "escalated", "reason": "Skill failed twice in this session."}
        else:
            result = {"status": "error", "reason": "Simulated skill failure."}
        self.audit.append({"user": user, "skill": skill, "status": result["status"]})
        return result

if __name__ == "__main__":
    runtime = Runtime()
    for attempt in range(1, 4):
        print(attempt, runtime.receive_task("student-1", "research", "summarize"))

