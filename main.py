from turtle import Screen
from food import Food
import time
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        snake.snake_grow()
        food.refresh()
        scoreboard.score_up()


    # detect collision with walls
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        snake.reset()
        scoreboard.reset_score()
        # game_is_on = False

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            snake.reset()
            scoreboard.reset_score()
            # game_is_on = False

screen.exitonclick()
