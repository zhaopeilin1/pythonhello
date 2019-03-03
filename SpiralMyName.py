#coding:utf-8
#SpiralMyName.py
import turtle
turtle.bgcolor("black")
t = turtle.Pen()
#
colors = ["red","blue","yellow","green"]
your_name=turtle.textinput("Enter your name","What is your name?")
for x in range(100):
    t.pencolor(colors[x%4])
    #t.circle(x)
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(your_name,font=("Arial",int((x+4)/4),"bold"))
    t.left(92)