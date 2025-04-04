import json
from tkinter import messagebox

DATA_FILE = "data.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_data(website, email, password):
    if not website or not password:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return False

    data = load_data()
    data[website] = {"email": email, "password": password}

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

    return True

def search_data(website):
    data = load_data()
    return data.get(website)
