#!/usr/bin/env python3

from tkinter import *
import pandas
from random import choice

# -------------- CONSTANTS --------------- #
BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 60, "bold")
current_position = {}
main_data = {}

# -------------- DATA --------------- #
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    o_data = pandas.read_csv("./data/german_words.csv")
    main_data = o_data.to_dict(orient="records")
else:
    main_data = data.to_dict(orient="records")

# -------------- FUNCTIONS --------------- #


def next_card():
    global current_position, flip_timer
    window.after_cancel(flip_timer)
    current_position = choice(main_data)
    canvas.itemconfig(card_color, image=card_front)
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_info, text=f"{current_position['German']}", fill="black")
    flip_timer = window.after(3000, flip)


def already_known():
    main_data.remove(current_position)
    new_main_data = pandas.DataFrame(main_data)
    new_main_data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


def flip():
    canvas.itemconfig(card_color, image=card_back)
    canvas.itemconfig(card_title, text="Portuguese", fill="white")
    canvas.itemconfig(card_info, text=f"{current_position['Portuguese']}", fill="white")


# -------------- WINDOW --------------- #
window = Tk()
window.title("Flash Card / German x Portuguese")
window.config(bg=BACKGROUND_COLOR, pady=20, padx=20)
flip_timer = window.after(3000, flip)

# -------------- CANVAS --------------- #
canvas = Canvas(width=800, height=530, highlightthickness=0, bg=BACKGROUND_COLOR)

card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")

card_color = canvas.create_image(400, 265, image=card_front)
card_title = canvas.create_text(400, 150, text="Title", font=FONT_LANGUAGE)
card_info = canvas.create_text(400, 263, text="word", font=FONT_WORD)

canvas.grid(column=0, row=0, columnspan=2)

# -------------- BUTTONS --------------- #
button_wrong = PhotoImage(file="./images/wrong.png")
button_x = Button(image=button_wrong, highlightthickness=0, command=next_card)

button_x.grid(column=1, row=1)

button_right = PhotoImage(file="./images/right.png")
button_y = Button(image=button_right, highlightthickness=0, command=already_known)

button_y.grid(column=0, row=1)

next_card()

window.mainloop()