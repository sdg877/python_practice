import random

figures = [
    "Leonardo da Vinci", "Cleopatra", "Nikola Tesla", "Ada Lovelace",
    "Socrates", "Genghis Khan", "Marie Curie", "Shakespeare",
    "Albert Einstein", "Joan of Arc", "Sun Tzu", "Isaac Newton"
]

roles = [
    "Chief Innovation Officer", "Head of Backend Operations",
    "VP of Strategy and Conquest", "Senior Metaphor Engineer",
    "Chief Alchemy Architect", "Director of Temporal R&D",
    "Full-Stack Visionary", "Quantum Outreach Specialist",
    "Lead Problem Definer", "Human-Centered Design Evangelist"
]

def assign_role():
    return f"{random.choice(figures)} – {random.choice(roles)}"

if __name__ == "__main__":
    print("Startup Team Assignments:\n")
    for _ in range(5):
        print(" -", assign_role())
