from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180
STARTING_POSITIONS = ((0, 0), (-20, 0), (-40, 0))


class Snake:
    """The snake that the player controls"""
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.create_segment(position)

    def create_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(position)
        self.snake.append(new_segment)

    def extend(self):
        self.create_segment(self.snake[-1].position())

    def reset_snake(self):
        for seg in self.snake:
            seg.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def move(self):
        """Constantly moves the snake forwards"""
        for seg_num in range(len(self.snake) - 1, 0, -1):
            self.snake[seg_num].goto(self.snake[seg_num - 1].pos())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Turns the head of the snake up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        """Turns the head of the snake right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        """Turns the head of the snake down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Turns the head of the snake left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
