# exit_program

def exit_program():
    print("Exiting...")
    sys.exit(0)
# update_leaderboard

def update_leaderboard(username, wpm):
    try:
        with open(LEADERBOARD_FILE_PATH, 'r') as file:
            leaderboard = json.load(file)
    except FileNotFoundError:
        leaderboard = []

    leaderboard.append({"username": username, "wpm": wpm})
    leaderboard = sorted(leaderboard, key=lambda x: x["wpm"], reverse=True)[:5]

    with open(LEADERBOARD_FILE_PATH, 'w') as file:
        json.dump(leaderboard, file)
# load_words_from_json

def load_words_from_json():
    try:
        with open(WORDS_FILE_PATH, 'r') as file:
            words_data = json.load(file)
            return words_data.get("words", [])
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error: Unable to load words. Please check the format of 'words.json'.")
        sys.exit(1)
# get_user_input

def get_user_input():
    try:
        return input("Type the words: ")
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
# main_logic

def main():
    print("Welcome to Terminal Typing Master!")
    username = get_username()

    while True:
        print("\nOptions:")
        print("1. Start Typing Test")
        print("2. Show Leaderboard")
        print("3. Exit")

        choice = input("Select an option (1/2/3): ")

        if choice == '1':
            words = load_words_from_json()
            random.shuffle(words)

            start_typing_test(words)

        elif choice == '2':
            show_leaderboard()

        elif choice == '3':
            exit_program()

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
if __name__ == "__main__":
    main()