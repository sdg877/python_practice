import random

prefixes = [
    "Aero", "Strixo", "Corvo", "Pluma", "Avio", "Falco", "Tetra", "Orni", "Buteo", "Psitta"
]

roots = [
    "dactyl", "phorus", "rhyncha", "pteryx", "gralla", "columba", "tyto", "melano", "leuco", "soma"
]

suffixes = [
    "ensis", "formis", "oides", "ianus", "ella", "alus", "ferus", "ornis", "avium", "raptor"
]

def generate_name():
    return random.choice(prefixes) + random.choice(roots) + random.choice(suffixes)

if __name__ == "__main__":
    print("🪶 Obscure Latin Bird Species Names:\n")
    for _ in range(10):
        print(" -", generate_name())
