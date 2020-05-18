# Simple Pong in Python 3 for Beginners
# Author: Benjamin McNabb AKA origami_pythonista

# Import Packages
import turtle
import time
import os

paused = False


def unpause():
    print("unpause() called")
    global paused
    paused = False


def pause():
    global paused
    paused = True
    while paused:
        time.sleep(0.1)

# Window
wn = turtle.Screen()
wn.title("pong by orgami_pythonista")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer()

# Score
score_a = 0
score_b = 0

# Players
player_a = wn.textinput("Player A", "Name of first player:")
player_b = wn.textinput("Player B", "Name of second player:")

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 4
ball.dy = 4

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("{}:{}  {}:{}".format(player_a, score_a, player_b, score_b), align="center", font=("Courier", 21, "normal"))


# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(unpause)
wn.onkeypress(pause, key="Space")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("{}:{}  {}:{}".format(player_a, score_a, player_b, score_b), align="center", font=("Courier", 21, "normal"))

    # Left and right
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("{}:{}  {}:{}".format(player_a, score_a, player_b, score_b), align="center", font=("Courier", 21, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() <paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    if (ball.xcor() < -340 and ball.xcor() < -350) and (ball.ycor() <paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    if score_a >= 10:
        winner = player_a
        pen.clear()
        pen.write("Game over, {} wins!".format(winner), align="center", font=("Courier", 21, "normal"))
        wn.exitonclick()
    elif score_b >= 10:
        winner = player_b
        pen.clear()
        pen.write("Game over, {} wins!".format(winner), align="center", font=("Courier", 21, "normal"))
        wn.exitonclick()
