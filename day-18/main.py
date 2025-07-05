from turtle import Turtle, Screen


tim = Turtle()
tim.shape("turtle")
tim.color("green")

# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)


# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


def shape(n):
    for _ in range(n):
        tim.forward(100)
        tim.left(360/n)

shape(8)

screen = Screen()
screen.exitonclick()