import random

adjectives1 = [
    "artless", "bawdy", "beslubbering", "churlish", "cockered",
    "craven", "droning", "fobbing", "gleeking", "mewling"
]

adjectives2 = [
    "base-court", "beef-witted", "clay-brained", "dizzy-eyed",
    "elf-skinned", "fat-kidneyed", "half-faced", "ill-nurtured"
]

nouns = [
    "apple-john", "barnacle", "bladder", "codpiece", "death-token",
    "dewberry", "flap-dragon", "hedge-pig", "scullion", "wagtail"
]

def generate_insult():
    return f"Thou {random.choice(adjectives1)}, {random.choice(adjectives2)} {random.choice(nouns)}!"

if __name__ == "__main__":
    print("🎭 Shakespearean Insults:\n")
    for _ in range(5):
        print(" -", generate_insult())
