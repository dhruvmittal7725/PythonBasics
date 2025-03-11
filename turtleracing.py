from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place Your Bet!", prompt="Enter a color from the Rainbow: ")
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
racers = []
winner = "red"

for i in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[i])
    tim.goto(-230, 130 - (i * 40))
    racers.append(tim)

is_on = True
while is_on:
    num = random.randint(0, 10)
    for racer in racers:
        racer.forward(num)
        cord = racer.xcor()
        if cord > 230:
            winner = racer.pencolor()
            is_on = False


print(f"The Winner is {winner}")
if winner == user_bet.lower():
    print("You win the Bet.")
else:
    print("You lose the Bet. Better luck Next time.")

screen.exitonclick()
