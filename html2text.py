#coding:utf-8
from goose3 import Goose
from goose3.text import StopWordsChinese
url  = 'http://www.bbc.co.uk/zhongwen/simp/chinese_news/2012/12/121210_hongkong_politics.shtml'
g = Goose({'stopwords_class': StopWordsChinese})
article = g.extract(url=url)
print article.cleaned_text[:150]
