#!/usr/bin/env python3

import time
from turtle import Screen
from game_logic.player import Player
from game_logic.car_manager import CarManager
from game_logic.scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing Road")
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)
screen.listen()

tommy = Player()
screen.onkey(key="Up", fun=tommy.move_forward)

score = Scoreboard()
car = CarManager()

game_is_on = True
while game_is_on:
    score.score_display()
    time.sleep(0.1)
    screen.update()

    car.create_cars()
    car.move()

    for i in car.all_cars:
        if i.distance(tommy.pos()) < 20:
            game_is_on = False
            score.game_over()

    if tommy.ycor() == 280:
        tommy.reset_player()
        car.increase_speed()
        score.CURRENT_LEVEL += 1

screen.exitonclick()
