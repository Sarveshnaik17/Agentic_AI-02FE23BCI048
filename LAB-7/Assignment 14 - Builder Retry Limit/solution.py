def run_builder(outcomes):
    attempts = 0
    trace = []
    while attempts < 2:
        attempts += 1
        status = outcomes[attempts - 1]
        trace.append(f"builder attempt {attempts}: {status}")
        if status == "success":
            return trace + ["continue to security_scan"]
        if attempts == 1:
            trace.append("retry once")
    return trace + ["escalate to human after retry limit"]

if __name__ == "__main__":
    print("Scenario A:", run_builder(["failure", "success"]))
    print("Scenario B:", run_builder(["failure", "failure"]))

