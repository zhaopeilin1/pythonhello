#coding:utf-8
#Rosette.py 任意多瓣花
import turtle
t=turtle.Pen()
number=int(turtle.numinput("花瓣数目","请输入花瓣数",6))
for x in range(number):
    t.circle(100)
    t.left(360/number)
