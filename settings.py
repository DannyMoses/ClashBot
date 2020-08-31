from dotenv import load_dotenv
from pathlib import Path  # Python 3.6+ only


def load_keys():
    key_path = Path('.') / 'keys.env'
    load_dotenv(key_path)
    print("DEBUg:", "Keys loaded!")


if __name__ == "__main__":
    load_keys()
    print("settings loaded!")
