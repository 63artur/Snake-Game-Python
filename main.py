import time
from turtle import Screen, Turtle
import random
import time
import snake
from food import Food
from score import Score
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake game")

snake = snake.Snake()
food = Food()
score = Score()
snake.make_turtle()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.all_turtles[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    if snake.all_turtles[0].xcor() > 280 or snake.all_turtles[0].xcor() < -280 or snake.all_turtles[0].ycor() > 280 or snake.all_turtles[0].ycor() < -280:
        score.reset_score()
        snake.reset()
    for turtle in snake.all_turtles[1:]:
        if snake.all_turtles[0].distance(turtle) < 10:
            score.reset_score()
            snake.reset()













screen.exitonclick()