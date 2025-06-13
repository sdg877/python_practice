import random

triggers = [
    "User adjusted system clock to 2071",
    "App launched before it was compiled",
    "Session expired before login",
    "File modified before creation",
    "Scheduled job executed retroactively",
    "Token invalidated in the past",
    "Build date occurs after deployment",
    "Crash logged in negative time"
]

effects = [
    "UI disappeared from historical record",
    "logs no longer align with observable reality",
    "database rejected timestamps from the future",
    "authentication occurred before credentials existed",
    "cache preemptively cleared itself",
    "system entered causal loop",
    "notifications arrived before trigger event",
    "deployment created a paradox in versioning"
]

def generate_bug_report():
    return f"{random.choice(triggers)} → {random.choice(effects)}"

if __name__ == "__main__":
    print("Time Travel Bug Reports:\n")
    for _ in range(5):
        print(" -", generate_bug_report())
