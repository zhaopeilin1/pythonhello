#coding:utf-8
#ColorMeSpiralled.py 定制名字螺旋线。如果每条线上的名字不同，需要输入名字数组
import turtle
turtle.bgcolor("black")
t = turtle.Pen()
#
colors = ["red","blue","yellow","green","orange","purple","gray","white"]
sides=int(turtle.numinput("","How many sides do you want(1-8)?",4,1,8))
your_name=turtle.textinput("Enter your name","What is your name?")
for x in range(100):
    t.pencolor(colors[x%4])
    #t.circle(x)
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(your_name,font=("Arial",int((x+4)/4),"bold"))
    t.left(92)