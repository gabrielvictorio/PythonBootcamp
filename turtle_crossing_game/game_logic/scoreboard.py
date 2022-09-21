from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.ht()
        self.CURRENT_LEVEL = 1

    def score_display(self):
        self.clear()
        self.goto(x=-290, y=260)
        self.write(align="left", arg=f"Level: {self.CURRENT_LEVEL}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(align="center", arg="GAME OVER", font=FONT)
