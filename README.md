# Terminal Typing Master

Welcome to the Terminal Typing Master, a simple typing test application in Python. This application allows users to test their typing speed by presenting a set of random words and measuring metrics such as words per minute (WPM).

## Prerequisites

- Python 3.x installed
- Basic understanding of file I/O, data structures (list, dictionaries), and JSON format.

## Getting Started

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd terminal-typing-master
   ```

3. Run the application:

   ```bash
   python main.py
   ```

## Features

### Username Input

- Prompt users to enter their username.

```python
# Example
Enter your username:
```

### Start Typing Test

- Initiate a typing test with random words.
- Measure and display typing metrics (Words Typed, Time Taken, WPM).

```python
# Example
Typing test starts now! Type the following words:
apple banana keyboard ...
```

### Show Leaderboard

- Display a leaderboard of top users based on their typing speed.

```python
# Example
Leaderboard:
user1: 80 WPM
user2: 75 WPM
...
```

### Exit Program

- Allow users to exit the program gracefully.

```python
# Example
Exiting...
```

### Update Leaderboard

- Update and sort the leaderboard stored in a JSON file.

### Load Words from JSON

- Load words from a JSON file into a Python dictionary.

## Future Perspectives

1. Add more typing categories.
2. Implement a time-based challenge mode.

## File Structure

- `main.py`: Main script containing the core logic and user interface.
- `username_input.py`: Function to capture user input for the username.
- `start_typing_test.py`: Functionality for starting and measuring typing tests.
- `show_leaderboard.py`: Displaying the leaderboard.
- `exit_program.py`: Graceful exit from the program.
- `update_leaderboard.py`: Updating and sorting the leaderboard.
- `load_words_from_json.py`: Loading words from a JSON file.
- `get_user_input.py`: Capturing user input.
  
## Acknowledgments

- This project was created as part of a learning exercise to practice Python programming.

Feel free to explore and contribute to make this typing test application even better!

---
