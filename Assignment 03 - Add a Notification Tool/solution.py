SIGNUPS = [8, 6, 10]
THRESHOLD = 10

def send_notification(message):
    return {"status": "drafted", "message": message, "sent": False}

def answer():
    average = sum(SIGNUPS) / len(SIGNUPS)
    trace = [{"tool": "calculator", "input": SIGNUPS, "output": average}]
    if average < THRESHOLD:
        draft = send_notification("Low turnout notice: please promote upcoming events.")
        trace.append({"tool": "send_notification",
                      "reason": f"Average {average:.1f} is below threshold {THRESHOLD}.",
                      "output": draft})
    return average, trace

if __name__ == "__main__":
    average, trace = answer()
    print(f"Average sign-ups: {average:.1f}")
    for entry in trace:
        print(entry)
    assert trace[-1]["output"]["sent"] is False

