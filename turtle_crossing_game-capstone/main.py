import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    screen.onkey(player.turtle_move, "Up")

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if player.distance(car) <= 25:
            scoreboard.game_over()
            game_is_on = False

    if FINISH_LINE_Y <= player.ycor():
        scoreboard.level += 1
        player.reached_goal()
        scoreboard.update_scoreboard()
        car_manager.increase_speed()

screen.exitonclick()