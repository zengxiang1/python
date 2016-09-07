#coding:utf-8

import urllib

param = {'firstname':'zx','lastname':'nihao'}
param = urllib.urlencode(param)

html = urllib.urlopen('http://pythonscraping.com/pages/files/processing.php',param).read()
print html