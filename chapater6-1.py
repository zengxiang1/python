from zipfile import ZipFile
from bs4 import BeautifulSoup
from urllib import urlopen
from io import BytesIO
wordFile = urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()
wordFile = BytesIO(wordFile)
document = ZipFile(wordFile)
xml_content = document.read('word/document.xml')
wordObj  = BeautifulSoup(xml_content.decode('utf-8'),"html.parser")
texts = wordObj.findAll("w:t")
for text in texts:
    print text.text

