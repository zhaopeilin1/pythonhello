#coding:utf-8
#import os
# 使用goose3 把html新闻网页html转化为文本，不含图片等多媒体。 可以用url 和 离线html文件
from goose3 import Goose
from goose3.text import StopWordsChinese
url  = 'http://world.people.com.cn/n1/2019/0305/c1002-30957989.html'
#html_file = 'c1002-30957989.html'
g = Goose({'stopwords_class': StopWordsChinese})
#article = g.extract(raw_html=open(html_file).read())
article = g.extract(url=url)
print(article.cleaned_text)

