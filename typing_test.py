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