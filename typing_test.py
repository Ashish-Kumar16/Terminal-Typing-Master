# start_typing_test

def start_typing_test(words_to_type):
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
