import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()
screen.listen()
screen.title("Turtle Crossing Game")
screen.onkey(player.up, 'Up')
screen.onkey(player.down, 'Down')




game_is_on = True
while game_is_on:
    time.sleep(0.1)
    scoreboard.show_score()
    screen.update()
    car_manager.create_car()
    car_manager.move(scoreboard.score)
    if player.finish_line():
        player.go_to_start()
        scoreboard.increase_score()

    for car in car_manager.all_cars:
        if car.distance(player) < 30:
            scoreboard.game_over()
            game_is_on = False



screen.exitonclick()
