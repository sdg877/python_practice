def run_definition_quiz(puzzle_data):
    print("\n📘 Definition: " + puzzle_data["question"])
    for idx, opt in enumerate(puzzle_data["options"], 1):
        print(f"{idx}. {opt}")
    choice = input("Your choice (1-4): ")
    try:
        if puzzle_data["options"][int(choice) - 1] == puzzle_data["answer"]:
            print("✅ Correct!")
        else:
            print(f"❌ Incorrect! The correct word was: {puzzle_data['answer']}")
    except:
        print("⚠️ Invalid input.")
