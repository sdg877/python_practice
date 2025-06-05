import json

def load_words(filepath='words.json'):
    with open(filepath, 'r') as file:
        return json.load(file)
