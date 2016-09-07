#coding:utf-8

from bs4 import BeautifulSoup as bs
from urllib import urlopn

def ngram(input,n):
	arr = input.split(' ')
	output = []
	for i in range(n,len(arr)-n+1):
		output.append(arr[i:i+n])

if __name__ == '__main__':
	html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
	bsObj = bs(html)
	content = bsObj.find("div",{"id","mw-content-text"}).getText