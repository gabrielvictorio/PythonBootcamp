#!/usr/bin/env python3

from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Georgia"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 8
MARK = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global timer, REPS,MARK
    window.after_cancel(timer)
    apple.itemconfig(meio, text=f"00:00")
    text_checkmark.config(text="")
    text_timer.config(text="Timer", foreground=GREEN)
    REPS = 8
    MARK = ""


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global REPS, MARK
    if REPS != 0:
        if REPS == 8 or REPS == 6 or REPS == 4 or REPS == 2:
            count_down(WORK_MIN*60)
            REPS -= 1
            text_timer.config(text="Work", foreground=GREEN)
            MARK += "✔"
            text_checkmark.config(text=f"{MARK}")
        elif REPS == 7 or REPS == 5 or REPS == 3:
            count_down(SHORT_BREAK_MIN*60)
            REPS -= 1
            text_timer.config(text="Short Break", foreground=PINK)
        elif REPS == 1:
            count_down(LONG_BREAK_MIN*60)
            REPS = 0
            text_timer.config(text="Long Break", foreground=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_min == 0:
        count_min = "00"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    apple.itemconfig(meio, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
# Window


window = Tk()
window.title("The Pomodoro Technique")
window.configure(padx=110, pady=60, background=YELLOW)
# Canvas
apple = Canvas(width=205, height=230, highlightthickness=0, bg=YELLOW)
apple_image = PhotoImage(file="tomato.png")
apple.create_image(103, 115, image=apple_image)
meio = apple.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, "30", "bold"))
apple.grid(column=1, row=2)
# Button
button_1 = Button(text="Start", command=start_timer)
button_1.grid(column=0, row=3)
button_2 = Button(text="Reset", command=reset_timer)
button_2.grid(column=3, row=3)
# Text Timer
text_timer = Label(text="Timer")
text_timer.grid(column=1, row=0)
text_timer.configure(padx=0, pady=10, background=YELLOW, font=(FONT_NAME, "40", "bold"), foreground=GREEN)

text_checkmark = Label()
text_checkmark.grid(column=1, row=4)
text_checkmark.configure(padx=0, pady=5, background=YELLOW, font=(FONT_NAME, "20", "bold"), foreground=GREEN)

window.mainloop()
