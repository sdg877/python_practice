import random

prefixes = [
    "Initiate the necessary procedures to", "Conduct an in-depth review and",
    "Formally allocate time to", "Evaluate the potential outcomes of attempting to",
    "Ensure thorough documentation is prepared before you", "As per protocol, proceed to",
    "Obtain stakeholder approval prior to any effort to", "Consider all possible implications before starting to"
]

basic_tasks = [
    "write tests", "clean the kitchen", "update dependencies", "send an email",
    "water the plants", "refactor code", "charge your phone", "push to GitHub",
    "read the docs", "rename the file"
]

def expand_task():
    return f"{random.choice(prefixes)} {random.choice(basic_tasks)}."

if __name__ == "__main__":
    print("Overly Detailed To-Do Tasks:\n")
    for _ in range(5):
        print(" -", expand_task())
