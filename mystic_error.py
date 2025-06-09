import random

verbs = [
    "Invocation failed", "Compilation disturbed", "Execution unraveled",
    "Binding incomplete", "Manifestation broken", "Script rejected"
]

causes = [
    "the scroll of dependencies was out of alignment",
    "the incantation required moonlight",
    "a daemon consumed the config file",
    "the compiler was cursed by a warlock",
    "your logic defied the laws of prophecy",
    "a sacred variable has vanished",
    "an oracle marked this loop as forbidden",
    "the runtime crossed into the shadow realm"
]

def generate_mystic_error():
    return f"{random.choice(verbs)} — {random.choice(causes)}."

if __name__ == "__main__":
    print("🔮 Mystic Error Messages:\n")
    for _ in range(5):
        print(" -", generate_mystic_error())
