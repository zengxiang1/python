#! /usr/bin/env python
# coding:utf-8
from urllib import urlopen

from bs4 import BeautifulSoup
import random
import re


pages = set()
def getLinks(url):
	global pages
	preUrl = "https://zh.wikipedia.org"
	urlcontent = preUrl+url
	print urlcontent
	html = urlopen(urlcontent)
	bsObj = BeautifulSoup(html,'html.parser')
	try:
		print bsObj.h1.get_text()
		print bsObj.find(id="wm-content-text").findAll("p")
		print bsObj.find(id="ca-edit").find("span")
	except AttributeError:
		print("error")
		print AttributeError
	for link in bsObj.findAll('a',href=re.compile("^(/wiki/)")):
		if 'href' in link.attrs:
			if link.attrs['href'] not in pages:
				newPages = link.attrs['href']
				print '------------'+newPages
				pages.add(newPages)
				getLinks(newPages)

getLinks("")

# getLinks("wiki/Kevin_Bacon")
# links  = getLinks("/wiki/Kevin_Bacon")
# while len(links) >0 :
# 	newArticle = links[random.randint(0,len(links)-1)].attrs['href']
# 	print newArticle
# 	getLinks(newArticle)