from turtle import Turtle, Screen
import random


def color_picker():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


direction = [0, 90, 180, 270]
dino = Turtle()
screen = Screen()
screen.colormode(255)
dino.speed("fastest")
for _ in range(90):
    dino.color(color_picker())
    dino.setheading(direction[random.randint(0, 3)])
    dino.setheading(_ * 4)
    dino.circle(100)
screen.exitonclick()
