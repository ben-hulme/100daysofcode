from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):

        self.chunks = []
        self.create_snake()
        self.head = self.chunks[0]

    def create_snake(self):

        x = 0
        y = 0

        for chunk in range(3):
            chunk = Turtle(shape="square")
            chunk.color("white")
            chunk.penup()
            chunk.goto(x, y)
            x -= 20
            self.chunks.append(chunk)

    def extend(self):
        chunk = Turtle(shape="square")
        chunk.color("white")
        chunk.penup()
        tail_loc = self.chunks[-1].pos()
        chunk.goto(tail_loc)
        self.chunks.append(chunk)


    def move(self):
        for seg_num in range(len(self.chunks) - 1, 0, -1):
            second_last_pos = self.chunks[seg_num - 1].pos()
            self.chunks[seg_num].goto(second_last_pos)
        self.head.forward(20)

    def direction_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def direction_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def direction_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def direction_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
