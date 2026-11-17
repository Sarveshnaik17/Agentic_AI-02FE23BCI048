WARNING_KW = 850
ALARM_KW = 1000

def classify_load(forecast_kw):
    if forecast_kw >= ALARM_KW:
        return "ALARM"
    if forecast_kw >= WARNING_KW:
        return "WARNING"
    return "NORMAL"

def recommend(forecast_kw, human_review=False):
    status = classify_load(forecast_kw)
    if status == "ALARM" and not human_review:
        return {"status": status, "action": "held for human review"}
    return {"status": status, "action": "schedule load reduction" if status == "ALARM" else "monitor"}

if __name__ == "__main__":
    print("Forecast 920 kW:", recommend(920))
    print("Forecast 1050 kW:", recommend(1050))
    print("After review:", recommend(1050, human_review=True))

