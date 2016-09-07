#cofing:utf-8

from urllib import urlopen
import re
from bs4 import BeautifulSoup
import pymysql

conn = pymysql.connect(user='root',host='localhost',passwd ='123456',charset='utf8' ,db='mysql')
cur = conn.cursor()
cur.execute('use wikipedia')

def pageIsExists(url):
	try:
		querySQL = 'select * from pages where url = %s'
		cur.execute(querySQL,(url))
		if cur.rowcount <=0:
			return False
		else:
			return cur.lastrowid
	except Exception, e:
		raise e

def insertPagesIfnotExists(url):
	global conn
	global cur
	try:
		querySQL = 'select * from pages where url = %s'
		cur.execute(querySQL,(url))
		if cur.rowcount <=0:
			insertSQL = 'insert into pages(url) values(%s)'
			cur.execute(insertSQL,(url))
			conn.commit()
			return cur.lastrowid
		else:
			return cur.fetchone()[0]
	except Exception, e:
		raise e
def insertLinkIfnotExists(fromPageId,toPageId):
	global conn
	global cur
	try:
		querySQL = 'select * from links where fromPageId = %s and toPageId =%s' 
		cur.execute(querySQL,(fromPageId,toPageId))
		if cur.rowcount <=0:
			insertSQL = 'insert into links(fromPageId,toPageId) values(%s,%s)'
			cur.execute(insertSQL,(fromPageId,toPageId))
			conn.commit()
	except Exception, e:
		raise e

def getLinks(link,level):
	if level > 4:
		return
	html = urlopen('https://en.wikipedia.org%s' % link)
	bsObj = BeautifulSoup(html,'html.parser')
	fromPageId = insertPagesIfnotExists(link)
	content = bsObj.find('div',{'id':'mw-content-text'})
	items = content.findAll('a',href=re.compile('^(/wiki/)((?!:).)*$'))
	for item in items:
		href = item.attrs['href']
		if not pageIsExists(href):
			insertLinkIfnotExists(fromPageId,insertPagesIfnotExists(href))
			getLinks(href,level+1)
			print 'new.............%s' % href
		else :
			print 'skip ---------- %s' % href
getLinks('/wiki/Kevin_Bacon',0)
