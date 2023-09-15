from turtle import Turtle, Screen
import randomcolor

tim = Turtle()
tim.shape("turtle")
tim.color("blue")
random_color = randomcolor.RandomColor()
# 360 / number of angles
# draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, and decagon


def draw_shape(sides, color):
    """Takes side parameters to create shape and color parameter."""
    for side in range(sides):
        tim.color(color)
        tim.right(360/sides)
        tim.forward(100)


for i in range(3, 11):
    draw_shape(i, random_color.generate())


screen = Screen()
screen.exitonclick()
