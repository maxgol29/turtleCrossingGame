import random
from turtle import Turtle
from random import choice, randint
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.create_car()

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(choice(COLORS))
            new_car.goto(300, randint(-250, 250))
            self.all_cars.append(new_car)

    def move(self, increment_by_score):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE + ((increment_by_score-1)*MOVE_INCREMENT))

