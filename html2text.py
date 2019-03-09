#coding:utf-8
#import os
# 使用goose3 把html新闻网页html转化为文本，不含图片等多媒体。 可以用url 和 离线html文件
from goose3 import Goose
from goose3.text import StopWordsChinese


onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

url  = 'http://world.people.com.cn/n1/2019/0305/c1002-30957989.html'
#html_file = 'c1002-30957989.html'
g = Goose({'stopwords_class': StopWordsChinese})
#article = g.extract(raw_html=open(html_file).read())
article = g.extract(url=url)
print(article.cleaned_text)

#从文件中取内容
def extractFromFile(html_file,g):
   article = g.extract(raw_html=open(html_file).read())
   return article.cleaned_text

#从url中取内容
def extractFromUrl(inputurl,g):
   article = g.extract(url=inputurl)
   return article.cleaned_text