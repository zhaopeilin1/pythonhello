#coding:utf-8
#MathHomework.py 3.6节python做作业
print("MathHOmework.py")
problem=input("请输入数学题，或者输入q退出：")
while(problem!="q"):
    print("对于题目:",problem,"答案是：",eval(problem))
    #重新读取用户输入，循环往复
    problem=input("请输入数学题，或者输入q退出：")
