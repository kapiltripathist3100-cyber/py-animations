import turtle
import math
import random


screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Starry Heart Outline")


t = turtle.Turtle()
t.speed(1000) 
t.penup()
t.hideturtle()

# List of colors for the stars
colors = ["red", "yellow", "blue", "green", "purple", "orange", "pink", "cyan", "magenta", "lime"]


def draw_star(size):
    t.pendown()
    
    c = random.choice(colors)
    t.color(c)
    t.fillcolor(c)
    
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()
    t.penup()


scale = 12 

# Loop through angles from 0 to 2*pi to plot the heart shape
# Stepping by 15 controls how densely the stars are packed
for i in range(0, 630, 8): 
    angle = i / 100.0
    
    # Parametric equations for a heart shape
    x = 16 * math.sin(angle)**3
    y = 13 * math.cos(angle) - 5 * math.cos(2*angle) - 2 * math.cos(3*angle) - math.cos(4*angle)
    
    # Move turtle to the calculated coordinate and draw a star
    t.goto(x * scale, y * scale)
    draw_star(10) # 10 is the size of the individual stars

# Keep the window open
turtle.done()
