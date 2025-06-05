import random

def generate_scramble(word):
    scrambled = ''.join(random.sample(word, len(word)))
    while scrambled == word:
        scrambled = ''.join(random.sample(word, len(word)))
    return scrambled

def generate_definition_quiz(word_list):
    correct = random.choice(word_list)
    options = [correct['word']]
    # Add 3 incorrect options
    while len(options) < 4:
        option = random.choice(word_list)['word']
        if option not in options:
            options.append(option)
    random.shuffle(options)
    return {
        "question": correct["definition"],
        "options": options,
        "answer": correct["word"]
    }
