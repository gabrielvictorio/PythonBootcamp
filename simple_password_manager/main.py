#!/usr/bin/env python3

from tkinter import *
from tkinter import messagebox
import random
import json


FONT = ("Courier", 11, "normal")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for n in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for char in range(random.randint(8, 10))]
    password_list += [random.choice(numbers) for char in range(random.randint(2, 4))]
    random.shuffle(password_list)

    password = "".join(password_list)

    user_input_password.insert(0, password)


def search_data():
    website = user_input_website.get()
    try:
        with open("data.json", 'r') as file:
            data = json.load(file)
            x = data[f"{website}"]["email"]
            y = data[f"{website}"]["password"]
    except KeyError:
        messagebox.showinfo(title="Warning", message=f"There's no information stored for the website {website}")
    except FileNotFoundError:
        messagebox.showinfo(title="Warning", message=f"There's no current data on the log. Please make an entry")
    else:
        messagebox.showinfo(title=f"{website}", message=f"Email: {x}\nPassword: {y}")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    password = user_input_password.get()
    email = user_input_email.get()
    website = user_input_website.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }

    }

    if len(password) == 0 or len(email) == 0 or len(website) == 0:
        messagebox.showinfo(title="Error", message="Please don't leave any fields empty")
    else:
        user_answer = messagebox.askyesno(title="Review before saving",
                                          message=f"Website: {website} \nEmail: {email} "
                                                  f"\nPassword: {password} \n\n Is everything ok?")
        if user_answer:
            try:
                with open("data.json", 'r') as file:
                    data = json.load(file)
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", 'w') as file:
                    json.dump(new_data, file, indent=4)
            else:
                with open("data.json", 'w') as file:
                    json.dump(data, file, indent=4)
            finally:
                user_input_password.delete(0, END)
                user_input_website.delete(0, END)
        else:
            user_input_password.delete(0, END)
            user_input_website.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.configure(padx=40, pady=40, bg="white")

canvas = Canvas(width=200, height=200, highlightthickness=0, bg="white")
lock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(column=1, row=0)

# Input Labels
label_website = Label(text="Website", font=FONT, bg="white")
label_website.grid(column=0, row=1)
label_email = Label(text="Email/Username", font=FONT, bg="white")
label_email.grid(column=0, row=2)
label_password = Label(text="Password", font=FONT, bg="white")
label_password.grid(column=0, row=3)

# Button
button_password = Button(text="Generate Password", command=password_generator)
button_password.grid(column=2, row=3)
button_search = Button(text="Search", command=search_data, width=14)
button_search.grid(column=2, row=1)
button_add_to_file = Button(text="Add", command=save, width=49)
button_add_to_file.grid(column=1, row=4, columnspan=2)

# Entry
user_input_website = Entry(width=38)
user_input_website.grid(column=1, row=1)
user_input_email = Entry(width=57)
user_input_email.grid(column=1, row=2, columnspan=2)
user_input_email.insert(0, "gabriel@outlook.com")
user_input_password = Entry(width=38)
user_input_password.grid(column=1, row=3)

window.mainloop()
