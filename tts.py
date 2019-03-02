#coding:utf-8
import pyttsx3
engine = pyttsx3.init()
engine.setProperty("voice","zh")
engine.say('韩子昂 高级驾驶员，北京第三区交通委提醒您：道路千万条，安全第一条。行车不规范，亲人两行泪!')
voices=engine.getProperty("voices")
#for item in voices:
#    print(item)
engine.say('富强，民主，文明，和谐！')
engine.runAndWait()