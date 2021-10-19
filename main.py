from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# Set screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create objects
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# Events
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Game loop
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food, add new food and increase current score by 1
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall and end the game
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_score()
        snake.reset_snake()

    # Detect collision with body part and end the game
    for part in snake.snake_body[1:]:  # except head
        if snake.head.distance(part) < 10:  # if "snake-head" distance from body part < 10
            scoreboard.reset_score()
            snake.reset_snake()

screen.exitonclick()
