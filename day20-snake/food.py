from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed(0)
        self.random_location()

    def random_location(self):
        random_x = round(random.randint(-280, 280) / 10) * 10
        random_y = round(random.randint(-280, 280) / 10) * 10
        if random_x % 20 != 0:
            random_x += 10
        if random_y % 20 != 0:
            random_y += 10
        self.goto(random_x, random_y)