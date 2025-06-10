import random

abilities = [
    "turn invisible", "read minds", "talk to plants", "teleport", "fly",
    "see the future", "talk to machines", "hear Wi-Fi", "control time", "glow in the dark"
]

limitations = [
    "only while sneezing", "but only to ducks", "only when nobody is watching",
    "in reverse", "only underwater", "but only on Tuesdays",
    "only in ancient Greek", "if holding a banana", "but forgets immediately after",
    "only while humming show tunes"
]

def generate_superpower():
    return f"Can {random.choice(abilities)}, {random.choice(limitations)}."

if __name__ == "__main__":
    print("🦸 Useless Superpowers:\n")
    for _ in range(5):
        print(" -", generate_superpower())
