from turtle import Turtle

ALIGNMENT = "center"
FONT = ("CourierStd", 12)


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0

        self.penup()
        self.speed(0)
        self.hideturtle()
        self.color("White")
        self.goto(0, 280)
        self.write(f"Score: {self.current_score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.current_score += 1
        self.clear()
        self.write(f"Score: {self.current_score}", align=ALIGNMENT, font=FONT)

    def end_game(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
