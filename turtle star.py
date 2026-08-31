from turtle import *
color('red')
fillcolor('yellow')
begin_fill()
start = pos()

while True:
    forward(200)
    left(170)
    if distance(start) < 1:
        break
end_fill()

