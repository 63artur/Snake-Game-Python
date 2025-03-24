from turtle import Turtle, Screen
class Snake:
    def __init__(self):
        self.positions = [0, -20, -40]
        self.all_turtles = []
    def make_turtle(self):
        for turtle_index in range(0, 3):
            new_turtle = Turtle(shape="square")
            new_turtle.penup()
            new_turtle.color('white')
            new_turtle.goto(self.positions[turtle_index], 0)
            self.all_turtles.append(new_turtle)
    def create_turtle(self):
        for position in self.positions:
            self.add_turtle(position)
    def add_turtle(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.penup()
        new_turtle.color('white')
        new_turtle.goto(position)
        self.all_turtles.append(new_turtle)
    def move(self):
        for turtle in range(len(self.all_turtles) - 1, 0, -1):
            new_x = self.all_turtles[turtle - 1].xcor()
            new_y = self.all_turtles[turtle - 1].ycor()
            self.all_turtles[turtle].goto(new_x, new_y)
        self.all_turtles[0].forward(20)
    def extend(self):
        self.add_turtle(self.all_turtles[-1].position())
    def up(self):
        if self.all_turtles[0].heading() != 270:
            self.all_turtles[0].setheading(90)
    def down(self):
        if self.all_turtles[0].heading() != 90:
            self.all_turtles[0].setheading(270)
    def left(self):
        if self.all_turtles[0].heading() != 0:
            self.all_turtles[0].setheading(180)
    def right(self):
        if self.all_turtles[0].heading() != 180:
            self.all_turtles[0].setheading(0)
    def reset(self):
        for seg in self.all_turtles:
            seg.goto(1000,1000)
        self.all_turtles.clear()
        self.make_turtle()