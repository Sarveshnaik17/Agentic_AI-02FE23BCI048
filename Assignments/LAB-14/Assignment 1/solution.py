def triage_skill(issue):
    if "locked" in issue.lower() or "sign in" in issue.lower():
        return "Check account status and sign-in error details."
    return "Collect the error message and affected service."

def password_reset_skill(issue):
    return ("Use the official password-reset page and verify identity. "
            "Never ask the user to share their current password or one-time code.")

def route(issue):
    text = issue.lower()
    if "password" in text or "reset" in text:
        return {"node": "password_reset_skill", "answer": password_reset_skill(issue)}
    return {"node": "triage_skill", "answer": triage_skill(issue)}

if __name__ == "__main__":
    for issue in ("My account is locked and I cannot sign in.", "How do I reset my password?"):
        print(issue, "->", route(issue))

