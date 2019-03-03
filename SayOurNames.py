#encoding:utf-8
name = input("What is your name? ")
while name!= "":
    for x in range(100):
        print(name," add oil!",end= " ")
    print()
    name = input("请输入另一个名字，或者输入 [Enter] 键退出游戏")
print("谢谢您玩这个游戏！")