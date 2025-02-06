import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.speed = STARTING_MOVE_DISTANCE
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.turtlesize(stretch_wid=1, stretch_len=2)
            new_car.goto(310, random.randrange(-250, 250))
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT

# def __init__(self):
#     super().__init__()
#     self.shape("square")
#     self.color(random.choice(COLORS))
#     self.penup()
#     self.turtlesize(1, 2)
#     self.setheading(180)
#     self.goto(320, random.randrange(-250, 250))
#     self.velocity = STARTING_MOVE_DISTANCE
#     self.move()
#
# def move(self):
#     self.forward(self.velocity)
#
# def level_up(self):
#     self.velocity += MOVE_INCREMENT
#     self.forward(self.velocity)
