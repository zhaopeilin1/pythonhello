#encoding:utf-8
#流浪地球运载车小程序 输入你的名字，生成北京第三区交通委提醒
import pyttsx3
engine = pyttsx3.init()
engine.setProperty("voice","zh")
#engine.say('韩子昂 高级驾驶员，北京第三区交通委提醒您：道路千万条，安全第一条。行车不规范，亲人两行泪!')
#engine.runAndWait()
#voices = engine.getProperty('voices')
#name = "刘启"
name = input("What is your name? ")
#for voice in voices:
#    print(voice.id,voice)
#    engine.setProperty('voice', voice.id)
#    engine.say(name)
    


while name!= "":
    for x in range(3):
        engine.say(name+' 高级驾驶员，北京第三区交通委提醒您：道路千万条，安全第一条。行车不规范，亲人两行泪!')
        engine.runAndWait()
    print()
    name = input("请输入另一个名字，或者输入 [Enter] 键退出游戏")
print("感谢您玩这个游戏！")
