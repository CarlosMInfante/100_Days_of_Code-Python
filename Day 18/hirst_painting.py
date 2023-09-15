# #  Make colors into tuples
# from colorgram import extract
#
# colors = extract('image.jpeg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
#
# print(rgb_colors)

# Use Turtle to make a painting that is 10 x 10.
# Dots are 20 siz and 50 apart.

import turtle as t
import random as r

t.colormode(255)
tim = t.Turtle()
tim.speed(0)
color_list = [(240, 230, 68), (182, 19, 42), (219, 238, 244), (187, 74, 36), (251, 230, 235), (18, 139, 86),
              (114, 180, 206), (25, 120, 166), (190, 179, 23), (218, 61, 97),  (206, 164, 91), (27, 39, 74),
              (76, 173, 98), (176, 46, 64), (38, 44, 112), (238, 232, 3), (18, 164, 211), (216, 133, 155),
              (212, 72, 54), (126, 184, 127), (8, 55, 37), (12, 93, 55), (236, 157, 177), (165, 29, 26),
              (148, 209, 221), (8, 86, 109), (161, 210, 186), (234, 172, 164)]

tim.penup()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)


def draw_row(count):
    for _ in range(count):
        tim.dot(20, r.choice(color_list))
        tim.penup()
        tim.forward(50)
    next_row()


def next_row():
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)


for _ in range(10):
    draw_row(10)

tim.hideturtle()


screen = t.Screen()
screen.exitonclick()


