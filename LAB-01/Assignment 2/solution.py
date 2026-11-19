def read_existing_schedule():
    return {"busy_days": ["Tuesday", "Wednesday"]}

def finalize_plan(unavailable_days):
    busy = set(read_existing_schedule()["busy_days"])
    unavailable = set(unavailable_days)
    conflicts = sorted(busy - unavailable)
    if conflicts:
        print("Conflict detected: " + ", ".join(conflicts) + ". Plan not finalized.")
        return None
    weekdays = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
    print("Plan finalized.")
    return {"status": "finalized", "available_days": sorted(weekdays - unavailable)}

if __name__ == "__main__":
    assert finalize_plan(["Sunday"]) is None

