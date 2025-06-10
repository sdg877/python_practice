import random

openers = [
    "The stack", "The method", "This variable", "The loop", "An exception", "The pointer",
    "A reference", "The memory", "This process", "That function"
]

actions = [
    "overflows", "vanishes", "awakens", "recurses endlessly", "has no form",
    "is undefined", "was never meant to be", "halts silently", "whispers nothing", "returns void"
]

philosophies = [
    "like a stone in the stream.",
    "as the river floods the valley.",
    "for all things must end.",
    "like echoes in an empty shell.",
    "as the moon forgets the tide.",
    "in the silence between thoughts.",
    "when the compiler finds itself.",
    "as memory dreams of structure.",
    "without warning, like the wind.",
    "as time eats the call stack."
]

def compose_zen_error():
    return f"{random.choice(openers)} {random.choice(actions)}, {random.choice(philosophies)}"

if __name__ == "__main__":
    print("🧘 Zen Error Messages:\n")
    for _ in range(5):
        print(" -", compose_zen_error())
