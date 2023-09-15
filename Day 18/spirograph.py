import turtle as t
from random import randint

tim = t.Turtle()
tim.shape("turtle")
t.colormode(255)
tim.speed(0)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color_tuple = (r, g, b)
    return random_color_tuple


def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)


screen = t.Screen()
screen.exitonclick()
