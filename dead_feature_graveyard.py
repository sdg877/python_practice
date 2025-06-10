import random

features = [
    "Teleportation Scheduler", "Mood-Based CSS Engine", "Quantum Logout Button",
    "Autonomous Clippy Clone", "Syntax Suggestion Ouija Board",
    "Self-Aware Captcha", "AI-Generated Bug Creator", "Real-Time Paperclip Tracker",
    "Postmodern XML Parser", "Invisible Scrollbar Telemetry"
]

reasons = [
    "caused irreparable timeline distortion",
    "was deemed sentient and filed for unionization",
    "violated three laws of thermodynamics",
    "consumed 98% of system memory on idle",
    "kept rewriting its own documentation",
    "disagreed with the product vision",
    "became self-referential and recursive",
    "passed a Turing test we didn’t ask for",
    "interfered with developer sleep cycles",
    "was only supported in Netscape Navigator"
]

def generate_entry():
    return f"{random.choice(features)} — {random.choice(reasons)}."

if __name__ == "__main__":
    print("Dead Feature Graveyard:\n")
    for _ in range(5):
        print(" -", generate_entry())
