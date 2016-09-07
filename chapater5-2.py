#coding:utf-8
from urllib import urlopen
import pymysql
from bs4 import BeautifulSoup
import re
conn = pymysql.connect(host='localhost',user='root',passwd='123456',charset='utf8',db='wikipedia')
cur = conn.cursor()


def isRepeat(url):
	global cur
	querySQL = "SELECT * FROM pages WHERE url = '%s'" % url
	print querySQL
	cur.execute(querySQL)
	if cur.rowcount == 0:
		return False
	return cur.fetchone()
def insertPage(url):
	global cur
	global conn
	try:
		querySQL = "select * from pages where url = \'%s\'" % url
		print querySQL
		cur.execute(querySQL)
		if cur.rowcount == 0:
			insertSQL  = "insert into pages(url) values('%s')" % url
			print insertSQL
			cur.execute(insertSQL)
			conn.commit()
			print cur.lastrowid
			return cur.lastrowid
		else:
			return cur.fetchone()[0]
	except Exception, e:
		return cur.fetchone()[0]

def insertLinks(fromPage,toPage):
	global cur
	global conn
	try:
		querySQL = 'select * from links where fromPageId =%s and toPageId =%s' % (fromPage,toPage)
		print querySQL
		cur.execute(querySQL)
		if cur.rowcount == 0:
			insertSQL = "insert into links(fromPageId,toPageId) values(%s,%s)" % (fromPage,toPage)
			print insertSQL
			cur.execute(insertSQL)
			conn.commit()
	except Exception, e:
		raise e
def getLinks(link,Deeplevel):
	ids = insertPage(link)
	if Deeplevel > 6:
		return;
	html = urlopen("https://zh.wikipedia.org%s" % link)
	bsObj = BeautifulSoup(html,'html.parser')
	hrefs = bsObj.find_all('a',href=re.compile("^(/wiki/)((?!:).)*$"))
	for href in hrefs:
		href = href.attrs['href']
		print type(href)
		insertLinks(ids,insertPage(href))
		if not isRepeat(href):
			getLinks(href,Deeplevel+1)
		else:
			print 'skip %s' % href

		

getLinks('/wiki/Rain',0)
