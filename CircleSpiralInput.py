#coding:utf-8
#CircleSpiralInput.py 圆螺旋线 
import turtle
turtle.bgcolor("black")
t = turtle.Pen()
colors = ["red","blue","yellow","green","orange","purple","gray","white"]

sides=int(turtle.numinput("","How many sides do you want(1-8)?",4,1,8))

for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x*3/sides+x)
    t.circle(x)
    t.left(360/sides+1)
    t.left(90)
    t.width(x*sides/200)

