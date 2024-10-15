from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.x_move = 15
        self.y_move = 15
        self.ball_speed = 0.06

    def ball_move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def wall_check(self, paddle1, paddle2):
        if self.ycor() > 280 or self.ycor() < -280 :
            self.bounce()
            return True
        elif self.xcor() > 400 and self.distance(paddle1) <50 or self.xcor() < -400 and self.distance(paddle2) < 50:
            self.x_move *= -1
            self.ball_speed *= 0.9
            return True
        else:
            return True

    def goal(self):
        self.reset()
        self.ball_speed = 0.06
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move *= -1
        self.ball_move()



