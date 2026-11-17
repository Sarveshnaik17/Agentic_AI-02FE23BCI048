def authorize_action(severity, action, risk_level):
    if action == "rollback":
        return "approval required"
    if severity == "WARNING" and action == "restart_single_pod" and risk_level == "low":
        return "executed automatically"
    return "approval required"

if __name__ == "__main__":
    cases = [
        ("WARNING", "restart_single_pod", "low"),
        ("WARNING", "rollback", "low"),
        ("ALARM", "restart_single_pod", "low"),
    ]
    for case in cases:
        print(case, "->", authorize_action(*case))

