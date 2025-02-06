import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

WIDTH = 600
HEIGHT = 600
X_BOUNDS = WIDTH / 2
Y_BOUNDS = HEIGHT / 2
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("Crossing Game")
screen.tracer(0)
turtle = Player()
scoreboard = Scoreboard(X_BOUNDS, Y_BOUNDS)
car_manager = CarManager()
screen.listen()
screen.onkey(turtle.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    if turtle.finish_line():
        scoreboard.level_up()
        car_manager.increase_speed()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            game_is_on = False
            print(car.distance(turtle))
            print("car - turtle", car.xcor() - turtle.xcor(), car.ycor() - turtle.ycor())
            # print("turtle", turtle.xcor(), turtle.ycor())
            scoreboard.game_over()

screen.exitonclick()
