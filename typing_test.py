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

def start_typing_test(words_to_type, username):
    print("\nTyping test starts now! Type the following words:")

    for word in words_to_type:
        print(word, end=" ", flush=True)
        time.sleep(1)  # Adjust the delay time if needed
    print()

    start_time = time.time()
    words_typed = get_user_input()
    end_time = time.time()

    typed_words_list = words_typed.split()
    total_words = len(words_to_type)
    correct_words = sum(w1 == w2 for w1, w2 in zip(words_to_type, typed_words_list))
    wrong_words = total_words - correct_words

    time_taken = end_time - start_time
    words_per_minute = int((len(words_typed.split()) / time_taken) * 60)
    accuracy = (correct_words / total_words) * 100

    print(f"\nWords Typed: {len(typed_words_list)}")
    print(f"Total Words: {total_words}")
    print(f"Correct Words: {correct_words}")
    print(f"Wrong Words: {wrong_words}")
    print(f"Accuracy: {round(accuracy, 2)}%")
    print(f"Time Taken: {round(time_taken, 2)} seconds")
    print(f"Words Per Minute: {words_per_minute} WPM")

    update_leaderboard(username, words_per_minute, accuracy)  


# show_leaderboard

def show_leaderboard():
    try:
        with open(LEADERBOARD_FILE_PATH, 'r') as file:
            leaderboard = json.load(file)
        print("\nLeaderboard:")
        for entry in leaderboard:
            username = entry['username']
            wpm = entry['wpm']
            accuracy = entry.get('accuracy', 'N/A')  # Use 'N/A' if 'accuracy' key is not present
            print(f"{username}: {wpm} WPM, Accuracy: {accuracy}%")
    except FileNotFoundError:
        print("\nLeaderboard is empty.")

# exit_program

def exit_program():
    print("Exiting...")
    sys.exit(0)

# update_leaderboard

def update_leaderboard(username, wpm, accuracy):
    try:
        with open(LEADERBOARD_FILE_PATH, 'r') as file:
            leaderboard = json.load(file)
    except FileNotFoundError:
        leaderboard = []

    leaderboard.append({"username": username, "wpm": wpm, "accuracy": accuracy})
    leaderboard = sorted(leaderboard, key=lambda x: x["wpm"], reverse=True)[:5]

    try:
        with open(LEADERBOARD_FILE_PATH, 'w') as file:
            json.dump(leaderboard, file)
    except Exception as e:
        print(f"Error updating leaderboard: {e}")

# load_words_from_json

def load_words_from_json():
    try:
        with open(WORDS_FILE_PATH, 'r') as file:
            words_data = json.load(file)
            words = words_data.get("words", [])
            return words
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