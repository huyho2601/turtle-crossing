import turtle
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color('red')
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.setup_position()

    def setup_position(self):
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)
        print(self.position())

    def finish_line(self):
        if self.ycor() == FINISH_LINE_Y:
            self.setup_position()
            return True
