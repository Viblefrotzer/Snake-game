from turtle import Turtle

start_position = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in start_position:
            self.add_segment(position)

    def add_segment(self, position):
        snake_body = Turtle(shape="square")
        snake_body.color("white")
        snake_body.penup()
        snake_body.goto(position)
        self.segments.append(snake_body)

    def snake_grow(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for part in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[part - 1].xcor()
            new_y = self.segments[part - 1].ycor()
            self.segments[part].goto(new_x, new_y)

        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset(self):
        for segment in self.segments:
            segment.ht()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
