WARNING = 70
ALARM = 85

def recommend(readings):
    if any(value >= ALARM for value in readings):
        return "human review required: ALARM threshold reached"
    consecutive_warnings = 0
    previous = None
    for value in readings:
        if value >= WARNING and (previous is None or value > previous):
            consecutive_warnings += 1
        else:
            consecutive_warnings = 0
        if consecutive_warnings >= 3:
            return "schedule_inspection"
        previous = value
    return "continue_monitoring"

if __name__ == "__main__":
    readings = [72, 76, 81]
    print("Readings:", readings, "Recommendation:", recommend(readings))
    assert max(readings) < ALARM

