class Planner:
    def __init__(self):
        self.plan = {"Tuesday": {"time": "17:00-19:00", "hours": 2}, "Friday": {"time": "17:00-19:00", "hours": 2}}
        self.original = self.plan
        self.log = []

    def revise(self, feedback):
        if "tuesday" in feedback.lower() and "evening" in feedback.lower():
            self.plan["Tuesday"]["time"] = "20:00-22:00"
        if "friday" in feedback.lower() and "one hour" in feedback.lower():
            self.plan["Friday"].update(time="17:00-18:00", hours=1)
        self.log.append({"iteration": len(self.log) + 1, "feedback": feedback,
                         "same_object": self.plan is self.original,
                         "plan": {day: value.copy() for day, value in self.plan.items()}})

if __name__ == "__main__":
    planner = Planner()
    planner.revise("Move Tuesday's session to the evening.")
    planner.revise("Also make Friday's session shorter, only one hour.")
    assert len(planner.log) == 2 and all(row["same_object"] for row in planner.log)
    for row in planner.log:
        print(row)

