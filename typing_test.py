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
