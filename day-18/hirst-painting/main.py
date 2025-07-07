from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("green")

screen = Screen()
screen.colormode(255)

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

tim.setposition(-10, -10)
x_coord = -screen.window_width() / 2 + 20 # Add a small offset from the edge
y_coord = -screen.window_height() / 2 + 20 # Add a small offset from the edge
tim.penup()
tim.goto(x_coord, y_coord)

for _ in range(10):
    tim.pendown()
    for _ in range(10):
        tim.pencolor(random.choice(color_list))
        tim.dot(20)
        tim.penup()
        tim.forward(50)
        tim.pendown()
    tim.penup()
    y_coord += 40
    tim.goto(x_coord, y_coord)
    



screen.exitonclick()


