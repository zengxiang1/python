#! /usr/bin/env python
# coding:utf-8
from urllib import urlopen

from bs4 import BeautifulSoup
import random
import re

def getLinks(url):
	preUrl = "https://en.wikipedia.org"
	urlcontent = preUrl+url
	print urlcontent
	html = urlopen(urlcontent)
	bsObj = BeautifulSoup(html,'html.parser')
	arr = bsObj.find('div',{'id':'bodyContent'}).findAll('a',href=re.compile("^(/wiki/)((?!:).)*$"))
	return arr

# getLinks("wiki/Kevin_Bacon")
links  = getLinks("/wiki/Kevin_Bacon")
while len(links) >0 :
	newArticle = links[random.randint(0,len(links)-1)].attrs['href']
	print newArticle
	getLinks(newArticle)