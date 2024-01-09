# get_user_input

def get_user_input():
    try:
        return input("Type the words: ")
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
