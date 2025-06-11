import random

intros = [
    "An app that", "A service that", "A platform designed to",
    "A tool for", "A web-based solution that", "A cloud-native platform that"
]

features = [
    "records your sleeping sounds", "automatically sends your thoughts to Slack",
    "tracks your coworkers' screen time", "replaces your keyboard with voice commands",
    "scores your facial expressions during meetings", "monitors your fridge usage patterns",
    "predicts your next burnout", "lets your boss remotely pause your Wi-Fi",
    "posts your calendar publicly", "archives all your eye contact moments"
]

justifications = [
    "to increase productivity", "for team alignment", "because transparency builds trust",
    "so you can optimize your workflow", "to reduce decision fatigue", 
    "to help HR flag anomalies", "in the spirit of openness", 
    "because someone had to do it", "to disrupt wellness tracking", "for compliance"
]

def generate_idea():
    return f"{random.choice(intros)} {random.choice(features)} {random.choice(justifications)}."

if __name__ == "__main__":
    print("Mildly Concerning App Ideas:\n")
    for _ in range(5):
        print(" -", generate_idea())
