from turtle import Turtle, Screen
import random


rgb_colors = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.speed("fastest")
x = -225
y = -225
tim.penup()
for i in range(10):
    tim.goto(x, y + (i * 50))
    for _ in range(10):
        color = rgb_colors[random.randint(0, len(rgb_colors) - 1)]
        tim.forward(50)
        tim.dot(20, color)
tim.hideturtle()
screen.exitonclick()
