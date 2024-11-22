from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
import os
from dotenv import load_dotenv

load_dotenv()



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbol + password_numbers




    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(END, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def dump_data(data, file):
    json.dump(data, file, indent=4)


def save():
    website_data = website_input.get()
    mail_data = mail_input.get()
    password_data = password_input.get()
    new_data = {website_data:{
        "email": mail_data,
        "password": password_data
    }}

    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
                # f.write(f"{website_data}: {mail_data}:{password_data}\n")
        except ValueError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)
        finally:
            website_input.delete(0, 'end')
            password_input.delete(0, 'end')

def search():
    website_data = website_input.get()

    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website_data in data:
            email = data[website_data]["email"]
            password = data[website_data]["password"]
            messagebox.showinfo(title=website_data, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website_data} exists.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_input = Entry(width=21)
website_input.focus()
website_input.grid(column=1, row=1)
search_btn = Button(text="Search", command=search, width=13)
search_btn.grid(column=2, row=1)

mail_label = Label(text="Email/Username:")
mail_label.grid(column=0, row=2)
mail_input = Entry(width=35)
mail_input.insert(END, os.environ["EMAIL"])
mail_input.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_input = Entry(width=21)
password_input.grid(column=1, row=3)
password_btn = Button(text="Generate Password", command=generate_password)
password_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()