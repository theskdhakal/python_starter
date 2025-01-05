from turtle import Screen
import time
from player import Player
from car_manager import CarManager





screen=Screen()
screen.setup(width=600,height=600)
screen.tracer(0)
screen.bgcolor("black")

car_manager=CarManager()

player=Player()

screen.listen()

screen.onkeypress(player.up,"Up")


game_is_on=True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()


    #detect collision with car:
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on=False

    #detect a successful crossing:
    if player.is_at_finish_line():
        player.go_to_start()







screen.exitonclick()