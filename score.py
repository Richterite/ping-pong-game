from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 19, "normal")
class Score_Pong(Turtle):
    def __init__(self, position, player_info):
        super(Score_Pong, self).__init__()
        self.score_player = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(position)
        self.update_score(player_info)

    def update_score(self, player_info):
        self.clear()
        self.write(f"{player_info}\n{self.score_player}",move= False,align=ALIGNMENT,font=FONT)
        self.score_player += 1


class Line(Turtle):
    def __init__(self):
        super(Line, self).__init__()
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(0,-300)
        self.setheading(90)
        self.pensize(width=5)
        self.draw_line()

    def draw_line(self):
        while self.ycor() < 300:
            self.pendown()
            self.fd(100)
            self.penup()



