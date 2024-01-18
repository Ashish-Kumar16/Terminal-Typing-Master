# Terminal Typing Master

**A simple typing test game to practice and improve your typing skills in the terminal.**

## Features

- **Typing Tests:** Challenge yourself with randomly generated word lists.
- **Leaderboard:** Track your progress and see how you stack up against others.
- **User-friendly Interface:** Easy to navigate and use.
- **Customizable Word Lists:** Add your own words to create personalized tests.

## Getting Started

1. **Install Required Modules:**
   ```bash
   pip install random time json sys
   ```
2. **Run the Program:**
   ```bash
   python typing_master.py
   ```

## Usage

1. **Enter your username.**
2. **Choose from the following options:**
   - **Start Typing Test:** Begin a typing test with a randomly generated word list.
   - **Show Leaderboard:** View the top scores and rankings.
   - **Exit:** Quit the program.

## Rules

- Type the words exactly as they are displayed, including capitalization and punctuation.
- Press Enter after typing the last word.
- Your typing speed (words per minute) and accuracy will be calculated and displayed.
- Your score will be saved to the leaderboard if you rank among the top 5.

## Additional Notes

- The word list is stored in a JSON file named `words.json`. You can modify this file to add or remove words.
- The leaderboard is stored in a JSON file named `leaderboard.json`.

**Have fun improving your typing skills!**
