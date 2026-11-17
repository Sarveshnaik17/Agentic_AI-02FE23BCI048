class Runtime:
    def __init__(self):
        self.counts = {}

    def run_task(self, user, task):
        return {"status": "completed", "task": task}

    def receive_task(self, user, task):
        count = self.counts.get(user, 0)
        if count >= 3:
            return {"status": "rejected", "reason": "Session limit of 3 tasks reached."}
        self.counts[user] = count + 1
        return self.run_task(user, task)

if __name__ == "__main__":
    runtime = Runtime()
    for number in range(1, 5):
        print(number, runtime.receive_task("student-1", f"task-{number}"))

