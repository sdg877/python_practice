import random

openers = [
    "You're surprisingly good at", "I never expected you to be capable of",
    "It’s impressive how well you hide your", "You really managed to make that",
    "You handled that better than usual for someone who", "That was almost as good as someone who usually",
    "You’ve really improved since you stopped", "It’s admirable how you didn’t let your"
]

endings = [
    "lack of experience.", "usual bad luck.", "tendency to overthink.", "complete absence of planning.",
    "previous failures stop you.", "natural awkwardness.", "habit of vanishing under pressure.",
    "instinct to panic take over.", "track record hold you back.", "sleep deprivation show."
]

def generate_compliment():
    return f"{random.choice(openers)} {random.choice(endings)}"

if __name__ == "__main__":
    print("Backhanded Compliments:\n")
    for _ in range(5):
        print(" -", generate_compliment())
