from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(snake.direction_up, "Up")
screen.onkey(snake.direction_down, "Down")
screen.onkey(snake.direction_left, "Left")
screen.onkey(snake.direction_right, "Right")
game_is_on = True


screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

screen.update()

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

# Detect Food Eaten
    if snake.head.distance(food.pos()) < 10:
        food.random_location()
        score.update_score()
        snake.extend()

# Detect Collision with Wall    
    for data in snake.head.pos():
        if data >= 300 or data <= -300:
            game_is_on = False
            score.end_game()
    
# Detect Tail Collision
    for data in snake.chunks[1:]:
        if snake.head.distance(data) < 10:
            game_is_on = False
            score.end_game()

screen.exitonclick()
