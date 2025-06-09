import random

audiences = [
    "wizards", "bards", "necromancers", "hobbits", "dragons", "druids",
    "orcish merchants", "elven royals", "wandering knights", "goblins"
]

products = [
    "potion delivery", "magical consulting", "scroll storage", "crystal-based communication",
    "rune encryption", "wand subscription box", "spell hosting", "enchanted artifact trading",
    "teleportation-on-demand", "bard streaming service"
]

buzzwords = [
    "AI-powered", "blockchain-based", "mobile-first", "decentralized", "cloud-native",
    "zero-trust", "gamified", "subscription-based", "serverless", "open-source"
]

def generate_startup():
    return f"{random.choice(buzzwords)} {random.choice(products)} service for {random.choice(audiences)}."

if __name__ == "__main__":
    print("🏰 Fantasy Startup Ideas:\n")
    for _ in range(5):
        print(" -", generate_startup())
