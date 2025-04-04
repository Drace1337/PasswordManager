from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button, messagebox
import os
from dotenv import load_dotenv
from password_manager.password import generate_password
from password_manager.storage import save_data, search_data

load_dotenv()

def save():
    website = website_input.get()
    email = mail_input.get()
    password = password_input.get()

    if save_data(website, email, password):
        website_input.delete(0, 'end')
        password_input.delete(0, 'end')

def search():
    website = website_input.get()
    data = search_data(website)

    if data:
        messagebox.showinfo(title=website, message=f"Email: {data['email']}\nPassword: {data['password']}")
    else:
        messagebox.showinfo(title="Error", message=f"No details for {website} exist.")

def setup_ui():
    global website_input, mail_input, password_input

    window = Tk()
    window.title("Password Manager")
    window.config(padx=50, pady=50)

    canvas = Canvas(width=200, height=200)
    pass_img = PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=pass_img)
    canvas.grid(column=1, row=0)

    Label(text="Website:").grid(column=0, row=1)
    website_input = Entry(width=21)
    website_input.grid(column=1, row=1)
    Button(text="Search", command=search, width=13).grid(column=2, row=1)

    Label(text="Email/Username:").grid(column=0, row=2)
    mail_input = Entry(width=35)
    mail_input.insert(0, os.getenv("EMAIL", ""))
    mail_input.grid(column=1, row=2, columnspan=2)

    Label(text="Password:").grid(column=0, row=3)
    password_input = Entry(width=21)
    password_input.grid(column=1, row=3)
    Button(text="Generate Password", command=lambda: password_input.insert(0, generate_password())).grid(column=2, row=3)

    Button(text="Add", width=36, command=save).grid(column=1, row=4, columnspan=2)

    window.mainloop()
