import random

reasons = [
    "the moon borrowed my WiFi",
    "my dreams were buffering",
    "time reversed itself briefly",
    "I misplaced reality",
    "the clouds needed debugging",
    "a ghost forked my code",
    "gravity took a sick day",
    "a sentient avocado judged me",
    "the laws of physics took PTO",
    "the metaphors escaped containment"
]

prefixes = [
    "I couldn’t make it because",
    "Sorry, I didn’t finish —",
    "I had to stop because",
    "Progress halted when",
    "The delay happened because"
]

def generate_excuse():
    return f"{random.choice(prefixes)} {random.choice(reasons)}."

if __name__ == "__main__":
    print("🌀 Surreal Excuses for Missing Work:\n")
    for _ in range(5):
        print(" -", generate_excuse())
