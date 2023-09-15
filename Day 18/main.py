from turtle import Turtle, Screen
#  import heroes

tim = Turtle()
tim.shape("turtle")
tim.color("blue")

# #  Drawing a square
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)

# #  installing heroes module
# print(heroes.gen())

#  Timmy drawing dashed line
for i in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen = Screen()
screen.exitonclick()
