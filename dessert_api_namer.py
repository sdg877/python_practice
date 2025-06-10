import random

adjectives = [
    "crispy", "frozen", "vanilla", "golden", "fluffy", "layered",
    "choco", "burnt", "spiced", "candied"
]

desserts = [
    "biscuit", "tart", "souffle", "mousse", "crumble", "pudding",
    "brownie", "eclair", "cake", "strudel"
]

suffixes = [
    "API", "Service", "Engine", "Client", "Module", "Interface"
]

def generate_name():
    return f"{random.choice(adjectives).capitalize()}{random.choice(desserts).capitalize()}{random.choice(suffixes)}"

if __name__ == "__main__":
    print("Random Dessert API Names:\n")
    for _ in range(5):
        print(" -", g
