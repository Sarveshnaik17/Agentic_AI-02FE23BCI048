SOURCES = [
    {"name": "Peer-reviewed study", "tier": 3, "claim": "No measurable effect in a preregistered trial."},
    {"name": "Vendor blog", "tier": 1, "claim": "Hallucinations fell by 35% in a product demo."},
]

def synthesize(sources):
    ranked = sorted(sources, key=lambda source: source["tier"], reverse=True)
    preferred = ranked[0]
    lower = ranked[-1]
    return (f"The synthesis leans toward {preferred['name']}: {preferred['claim']} "
            f"The lower-tier claim from {lower['name']} was down-weighted, not discarded: {lower['claim']}")

if __name__ == "__main__":
    print(synthesize(SOURCES))

