import random

verbs = [
    "Review", "Update", "Refactor", "Fix", "Document", "Test", "Check", "Clean", "Rename", "Move"
]

objects = [
    "internal config", "legacy comments", "temp folder", "unused variables",
    "API docs", "error logs", "dev notes", "permissions", "backup script", "build output"
]

contexts = [
    "before release", "just in case", "for consistency", "because it's messy",
    "as discussed", "with low priority", "quietly", "without breaking things",
    "after hours", "while nobody is looking"
]

def generate_task():
    return f"{random.choice(verbs)} {random.choice(objects)} {random.choice(contexts)}."

if __name__ == "__main__":
    print("Boring Task List:\n")
    for _ in range(5):
        print(" -", generate_task())
