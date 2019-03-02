#SquareSpiral1.py 
import turtle
turtle.bgcolor("black")
t = turtle.Pen()
colors = ["red","blue","yellow","green"]

for x in range(100):
    t.pencolor(colors[x%4])
    #t.circle(x)
    t.forward(x)
    t.left(91)
