PAYMENTS = {
    "logs": ["payment timeout rate 35%", "5xx responses rising"],
    "deploy": "release payments-api 2.4",
    "metrics": {"error_rate": 0.35},
}
POOL = {
    "logs": ["database pool wait queue growing", "connections near configured limit"],
    "deploy": "release reporting-worker 1.8",
    "metrics": {"pool_utilization": 0.92, "db_cpu": 0.55},
}

def classify_severity(incident):
    if incident["metrics"].get("error_rate", 0) >= 0.2:
        return "ALARM"
    if incident["metrics"].get("pool_utilization", 0) >= 0.85:
        return "WARNING"
    return "INFO"

def correlate_with_recent_changes(incident):
    joined = " ".join(incident["logs"]).lower()
    if "pool" in joined or "connections" in joined:
        return "database connection-pool exhaustion"
    return "payment API regression"

if __name__ == "__main__":
    for incident in (PAYMENTS, POOL):
        print({"diagnosis": correlate_with_recent_changes(incident),
               "severity": classify_severity(incident), "deploy": incident["deploy"]})

