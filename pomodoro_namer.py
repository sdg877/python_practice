import random

prefixes = [
    "The", "Operation", "Mission", "Project", "Code", "Quest for", "Return to"
]

themes = [
    "Focus", "Deep Work", "Flow State", "Distraction-Free Zone", "Silence", "Zen", "Brainstorm"
]

locations = [
    "Fortress", "Cave", "Sanctuary", "Lab", "Temple", "Arena", "Chamber", "Forge", "Barracks"
]

emojis = ["🧠", "⚔️", "🔥", "🪑", "📚", "☕", "💻"]

def generate_name():
    name = f"{random.choice(emojis)} {random.choice(prefixes)} {random.choice(themes)} {random.choice(locations)}"
    return name

if __name__ == "__main__":
    print("🍅 Pomodoro Session Names:\n")
    for _ in range(5):
        print(" -", generate_name())
