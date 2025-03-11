from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
program = True
def up():
    tim.forward(25)
def down():
    tim.backward(25)
def right():
    heading = tim.heading()
    tim.setheading(heading + 10)
def left():
    heading = tim.heading()
    tim.setheading(heading - 10)
def off():
    return False
def clear():
    tim.home()
    tim.clear()
screen.listen()
screen.onkey(key="w", fun=up)
screen.onkey(key="s", fun=down)
screen.onkey(key="d", fun=right)
screen.onkey(key="a", fun=left)
screen.onkey(key="c", fun=clear)
screen.onkey(key="e", fun=off)
screen.exitonclick()
