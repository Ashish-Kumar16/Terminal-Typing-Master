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
