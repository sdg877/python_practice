import random

starters = [
    "Always remember to", "Try to avoid", "Don’t underestimate the power of",
    "If possible,", "Make time to", "Never forget to", "It's wise to occasionally",
    "Without hesitation,", "You might benefit from", "It’s not a bad idea to"
]

actions = [
    "question your fridge’s motives", "rotate your indoor plants", "check under the bed twice",
    "rename your WiFi network weekly", "listen to elevator music intentionally",
    "apologize to your houseplants", "practice typing with your eyes closed",
    "read terms and conditions aloud", "wave at security cameras", "carry an empty folder with purpose"
]

def generate_advice():
    return f"{random.choice(starters)} {random.choice(actions)}."

if __name__ == "__main__":
    print("Unsolicited Life Advice:\n")
    for _ in range(5):
        print(" -", generate_advice())
