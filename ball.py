from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        # LOGIC:
        # here we just want to first move ball to the upward
        # so just we add the current value of x cor ,y cor
        # now as the value of x and y is increasing so the ball is also make graph of straight line ..

        random_x = self.xcor() + self.x_move
        random_y = self.ycor() + self.y_move
        self.goto(random_x, random_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def refresh(self):
        self.goto(0, 0)
        self.bounce_x()
