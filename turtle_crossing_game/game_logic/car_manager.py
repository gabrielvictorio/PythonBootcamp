from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.STARTING_MOVE_DISTANCE = 5
        self.MOVE_INCREMENT = 10
        self.ht()

    def create_cars(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2)
            new_car.setheading(180)
            new_car.sety(float(random.choice(range(-250, 250))))
            new_car.setx(300)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        self.STARTING_MOVE_DISTANCE += self.MOVE_INCREMENT
