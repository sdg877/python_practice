from word_loader import load_words
from puzzle_generator import generate_definition_quiz, generate_scramble
from game_engine import run_definition_quiz

def main():
    word_list = load_words()

    print("🎉 Welcome to the Obscure Word Puzzle Game!")
    while True:
        print("\nChoose a puzzle type:")
        print("1. Definition Quiz")
        print("2. Scramble Challenge")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            puzzle = generate_definition_quiz(word_list)
            run_definition_quiz(puzzle)
        elif choice == "2":
            word = random.choice(word_list)["word"]
            scrambled = generate_scramble(word)
            print(f"\n🔀 Unscramble the word: {scrambled}")
            answer = input("Your guess: ")
            if answer.lower() == word.lower():
                print("✅ Correct!")
            else:
                print(f"❌ Nope, it was: {word}")
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice.")

if __name__ == "__main__":
    main()
