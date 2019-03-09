#coding:utf-8
import os
# 使用goose3 把html新闻网页html转化为文本，不含图片等多媒体。 可以用url 和 离线html文件
from goose3 import Goose
from goose3.text import StopWordsChinese
from os import listdir
from os.path import isfile, join

mypath = '/data01/Downloads/webpages/'

#从文件中取内容
def extractFromFile(html_file,g):
   article = g.extract(raw_html=open(html_file).read())
   return article

#从url中取内容
def extractFromUrl(inputurl,g):
   article = g.extract(url=inputurl)
   return article.cleaned_text

#把文章写到txt文件，文件名传入，文件内容第一行是标题
def writeArticleTxt(fullpath,article):
    fo = open(fullpath, "w")
    fo.write(article.title+"\n")
    fo.write(article.cleaned_text)
    # 关闭打开的文件
    fo.close()

g = Goose({'stopwords_class': StopWordsChinese})


onlyfiles = [join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f))]

#url  = 'http://world.people.com.cn/n1/2019/0305/c1002-30957989.html'
#html_file = 'c1002-30957989.html'

#article = g.extract(raw_html=open(html_file).read())
count = 0;
for htmlFile in onlyfiles:
    article = extractFromFile(htmlFile,g)
    writeArticleTxt(mypath+"../webpages_clean/"+article.title.replace("/","_")+".txt",article)
    count += 1
    print(count)





