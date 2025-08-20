from turtle import Screen, Turtle
from paddles import Paddle
from ball import Ball
import time
from scoreboard import Score

screen = Screen()
screen.bgcolor('black')
screen.setup(800,600)
screen.title('My Pong Game')
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()


screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_on = True

while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() < -280 or ball.ycor() > 285:
        ball.bounce_wall()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_paddle()
        ball.move_speed *= 0.8


    if ball.xcor() > 400:
        ball.refresh()
        score.up("left")
        ball.move_speed = 0.03

    if ball.xcor() < -400:
        ball.refresh()
        score.up('right')
        ball.move_speed = 0.03

    if score.l_score == 3:
        score.game_over('Left')
        game_on = False
    elif score.r_score == 3:
        score.game_over('Right')
        game_on = False





screen.exitonclick()