from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen=Screen()
screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up,"Up")
screen.onkey(r_paddle.move_down,"Down")
screen.onkey(l_paddle.move_up,"w")
screen.onkey(l_paddle.move_down,"s")



is_game_on=True

while is_game_on:
    # less the time,sleep, faster is gonna be ball moving
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() >320 or ball.distance(l_paddle) <50 and ball.xcor() < -320:
        ball.bounce_x()


    # detect the paddle missing the ball
    if ball.xcor() > 380:
        ball.ball_reset()
        scoreboard.l_point()

    if ball.xcor() < -380:
       ball.ball_reset()
       scoreboard.r_point()



screen.exitonclick()