import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()
scoreboard.increment_score()
player = Player()
car_manager = CarManager()

screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(scoreboard.move_speed)
    screen.update()

    if player.ycor() >= 280:
        scoreboard.increment_score()
        player.goto(0, -280)

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if player.distance(car) < 25:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()