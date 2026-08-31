import turtle
import math
import colorsys


screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Radiating Heart Pattern")


t = turtle.Turtle()
t.speed(5)       
t.hideturtle()   

def heart_x(angle):
    return 16 * math.sin(angle) ** 3

def heart_y(angle):
    return 13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)


total_lines = 120
scale_factor = 15

for i in range(total_lines):
    
    angle = i * (math.pi * 2) / total_lines
    
    
    x = heart_x(angle) * scale_factor
    y = heart_y(angle) * scale_factor

    
    color = colorsys.hsv_to_rgb(i / total_lines, 1.0, 1.0)
    t.color(color)

    
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.goto(x, y)

    
    t.setheading(0)
    t.begin_fill()
    for _ in range(5):
        t.forward(6)
        t.right(144)
    t.end_fill()


turtle.done()
