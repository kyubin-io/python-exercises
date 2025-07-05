from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("green")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "LightSeaGreen", "Wheat", "SlateGray", "SeaGreen", "FloralWhite", "LightCoral", "SkyBlue", "CadetBlue", "Crimson"]

# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)


# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.left(angle)

# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)

directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()