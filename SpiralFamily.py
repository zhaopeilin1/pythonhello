#coding:utf-8
import turtle
turtle.bgcolor("black")
t = turtle.Pen()
#颜色列表
colors = ["red","blue","yellow","green","orange","purple","gray","white"
          ,"brown","pink"]
#家庭成员列表，后续往列表里添加成员
family=[]
#sides=int(turtle.numinput("","How many sides do you want(1-8)?",4,1,8))
name=turtle.textinput("My family","请输入一个名字，或者者按 [Enter] 键结束?")
while name!="":
    #添加成员名字
    family.append(name)
    name=turtle.textinput("My family","请输入一个名字，或者者按 [Enter] 键结束?")
for x in range(100):
    t.pencolor(colors[x%len(family)])
    #t.circle(x)
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(family[x%len(family)],font=("Arial",int((x+4)/4),"bold"))
    t.left(360/len(family)+2)