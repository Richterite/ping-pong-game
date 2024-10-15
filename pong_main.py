from turtle import Screen, Turtle
from pong_bar_real import Paddle
from ball import Ball
from score import Score_Pong, Line
import time
screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor("black")
screen.title("PING-POGGG")
screen.listen()
screen.tracer(0)



POSITION = [(420, 0), (-420, 0)]
player_1 = Paddle(POSITION[0])
player_2 = Paddle(POSITION[1])
# Player 1 control
screen.onkey(key="Up", fun=player_1.go_up)
screen.onkey(key="Down", fun=player_1.go_down)


# Player 2 Control
screen.onkey(key="w", fun=player_2.go_up)
screen.onkey(key="s", fun=player_2.go_down)

ball = Ball()
line = Line()
score_player1 = Score_Pong(position=(150, 220),player_info="Player 1")
score_player2 = Score_Pong(position=(-150, 220), player_info="Player 2")



def close_window():
    screen.bye()

# Exit button
screen.onkey(key='q', fun=close_window)

while ball.wall_check(player_1,player_2):
    screen.update()
    time.sleep(ball.ball_speed)
    ball.ball_move()
    if ball.xcor() > 430 or ball.xcor() < -430:
        if ball.xcor() < -430:
            score_player1.update_score("Player 1")
        elif ball.xcor() > 430:
            score_player2.update_score("Player 2")

        ball.goal()








screen.exitonclick()

# self.bar1 = [1, 2 ,3]
# self.bar2 = [1, 2, 3]
# def player1_control(self):
#     screen1 = Screen()
#     screen1.onkey(key="w", fun=self.go_up1)
#     # screen1.onkey(key="s", fun=self.go_down1)
#     return True
#
#
# def player2_control(self):
#     screen2 = Screen()
#     screen2.onkey(key="Up", fun=self.go_up2)
#     # screen2.onkey(key="Down", fun=self.go_down2)
#     return True
#
# def go_up(self):
#     if self.player1_control():
#         for position1 in range(len(self.bar1)-1, 0, -1):
#             new_x1 = self.bar1[position1 - 1].xcor()
#             new_y1 = self.bar1[position1 - 1].ycor()
#             self.bar1[position1].goto(new_x1, new_y1)
#         self.bar1[0].fd(20)
#     elif self.player2_control():
#         for position2 in range(len(self.bar2) - 1, 0 , -1):
#             new_x2 = self.bar2[position2 - 1].xcor()
#             new_y2 = self.bar2[position2 - 1].ycor()
#             self.bar2[position2].goto(new_x2, new_y2)
#         self.bar2[0].fd(20)
