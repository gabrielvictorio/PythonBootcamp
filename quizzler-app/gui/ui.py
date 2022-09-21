from tkinter import *
from game_logic.quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz:QuizBrain):
        self.quiz = quiz

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.label = Label(font=("Arial", "15", "normal"), text="Score: 0", fg="white", bg=THEME_COLOR)
        self.label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_tag = self.canvas.create_text(150, 120, width=250, text="Title", font=("Arial", "20", "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50, padx=20)

        button_false = PhotoImage(file="./images/false.png")
        self.button_f = Button(image=button_false, highlightthickness=0, command=self.false_button)
        self.button_f.grid(column=1, row=2)

        button_true = PhotoImage(file="./images/true.png")
        self.button_y = Button(image=button_true, highlightthickness=0, command=self.true_button)
        self.button_y.grid(column=0, row=2)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        self.label.config(text=f"Score: {self.quiz.score}")
        question = self.quiz.next_question()
        self.canvas.itemconfig(self.question_tag, text=question)

    def true_button(self):
        self.feedback(self.quiz.check_answer("true"))

    def false_button(self):
        self.feedback(self.quiz.check_answer("false"))

    def feedback(self, x):
        if x:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question())
