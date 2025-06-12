import random

word_starts = [
    "glim", "vor", "neth", "salu", "kren", "tash", "moro", "ilun", "drai", "vask"
]

word_ends = [
    "enth", "ari", "osk", "el", "urra", "ath", "iv", "ume", "enya", "orn"
]

definitions = [
    "the feeling of remembering something that never happened",
    "the quiet understanding shared by two people passing in a hallway",
    "the weight of a task you’ve chosen to delay without guilt",
    "the subtle ache of knowing a moment is becoming a memory",
    "the comfort found in familiar discomfort",
    "the pause before a decision you’ll definitely regret",
    "the warmth of light reflecting off something you forgot you loved",
    "a deep desire to explain something you know can’t be explained",
    "the mental fog that forms when you over-prepare for a conversation",
    "the peaceful frustration of solving a problem too late"
]

def generate_word():
    word = random.choice(word_starts) + random.choice(word_ends)
    definition = random.choice(definitions)
    return f"{word.capitalize()} — {definition}"

if __name__ == "__main__":
    print("Untranslatable Word Definitions:\n")
    for _ in range(5):
        print(" -", generate_word())
