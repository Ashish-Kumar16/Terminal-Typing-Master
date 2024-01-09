import random
import time
import json
import sys

WORDS_FILE_PATH = "words.json"
LEADERBOARD_FILE_PATH = "leaderboard.json"
# username_input

def get_username():
    return input("Enter your username: ")

# start_typing_test

def start_typing_test(words_to_type,username):
    print("\nTyping test starts now! Type the following words:")
    start_time = time.time()
    words_typed = get_user_input()
    end_time = time.time()

    time_taken = end_time - start_time
    words_per_minute = int((len(words_typed.split()) / time_taken) * 60)

    print(f"\nWords Typed: {len(words_typed.split())}")
    print(f"Time Taken: {round(time_taken, 2)} seconds")
    print(f"Words Per Minute: {words_per_minute} WPM")

    update_leaderboard(username, words_per_minute)

# show_leaderboard

def show_leaderboard():
    try:
        with open(LEADERBOARD_FILE_PATH, 'r') as file:
            leaderboard = json.load(file)
        print("\nLeaderboard:")
        for entry in leaderboard:
            print(f"{entry['username']}: {entry['wpm']} WPM")
    except FileNotFoundError:
        print("\nLeaderboard is empty.")

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

            start_typing_test(words,username)

        elif choice == '2':
            show_leaderboard()

        elif choice == '3':
            exit_program()

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
if __name__ == "__main__":
    main()