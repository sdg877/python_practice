import random

prefixes = [
    "Humbly", "Respectfully", "With sincere apologies,", "At your convenience,", 
    "With the utmost humility,", "Begging your pardon,"
]

verbs = [
    "addressed", "corrected", "resolved", "enhanced", "improved", "updated", "adjusted"
]

objects = [
    "a minor issue", "an unexpected behavior", "a small bug", "a slight oversight",
    "a tiny hiccup", "an inconsistency", "some suboptimal logic"
]

context = [
    "in the codebase", "within the application", "in the interface", 
    "during execution", "while handling requests", "in the backend logic"
]

def rewrite_commit(message):
    return f"{random.choice(prefixes)} {random.choice(verbs)} {random.choice(objects)} {random.choice(context)}. {message.strip().capitalize()}."

if __name__ == "__main__":
    test_input = "fix bug in api"
    print("🧼 Overly Polite Commit Rewrite:\n")
    print("Original:", test_input)
    print("Polite  :", rewrite_commit(test_input))
