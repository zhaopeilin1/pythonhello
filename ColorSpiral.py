#SquareSpiral1.py 
import turtle
turtle.bgcolor("black")
t = turtle.Pen()
sides=5
colors = ["red","blue","yellow","green","orange","purple"]

for x in range(100):
    t.pencolor(colors[x%sides])
    t.forward(x*3/sides+x)
    t.left(360/sides+1)
    t.left(90)
    t.width(x*sides/200)

