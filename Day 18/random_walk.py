import turtle as t
from random import choice, randint

tim = t.Turtle()
tim.shape("turtle")
t.colormode(255)
tim.pensize(15)
tim.speed(0)

# color = ["red", "green", "yellow", "blue", "purple", "orange", "LightSeaGreen"]
direction = [0, 90, 180, 270]


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color_tuple = (r, g, b)
    return random_color_tuple


for i in range(400):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(choice(direction))

screen = t.Screen()
screen.exitonclick()
