# load_words_from_json

def load_words_from_json():
    try:
        with open(WORDS_FILE_PATH, 'r') as file:
            words_data = json.load(file)
            return words_data.get("words", [])
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error: Unable to load words. Please check the format of 'words.json'.")
        sys.exit(1)
