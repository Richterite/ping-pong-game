from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, position):
        self.coordinate = position
        super(Paddle, self).__init__()
        self.create_bar(position)
        
    def create_bar(self, position_new):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position_new)

    def go_up(self):
        if not self.ycor() > 200:
            new_y = self.ycor() + 40
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if not self.ycor() < -200:
            new_y = self.ycor() - 40
            self.goto(self.xcor(), new_y)

    def bot_move(self):
        if self.ycor() < 200:
            while self.ycor() < 200:
                new_y = self.ycor() + 40
                self.goto(self.xcor(),new_y)
        elif self.ycor() > -200:
            while self.ycor() > -200:
                new_y = self.ycor() - 40
                self.goto(self.xcor(), new_y)

