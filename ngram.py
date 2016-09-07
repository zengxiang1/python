#coding:utf-8

import re
from urllib import urlopen
import operator

def cleaData(content):
	output = []
	content = re.sub("\n+"," ",content)
	content = re.sub(" +"," ",content)
	content = content.lower()
	content = content.split(' ')

	for i in range(0,len(content)):
		item = content[i]
		if len(item) > 1 or item =='i' or item =='a':
			output.append(item)
	return output
def ngram(content,level):
	content = cleaData(content)
	output = {}
	for i in range(0,len(content)-level+1):
		if not isCommon(content[i:i+level]):
			ngramTemp = " ".join(content[i:i+level])
			if ngramTemp not in output:
				output[ngramTemp] = 1
			else:
				output[ngramTemp] += 1
	return output

def isCommon(ngram):
	commonWords = ["the", "be", "and", "of", "a", "in", "to", "have", "it",
	"i", "that", "for", "you", "he", "with", "on", "do", "say", "this",
	"they", "is", "an", "at", "but","we", "his", "from", "that", "not",
	"by", "she", "or", "as", "what", "go", "their","can", "who", "get",
	"if", "would", "her", "all", "my", "make", "about", "know", "will",
	"as", "up", "one", "time", "has", "been", "there", "year", "so",
	"think", "when", "which", "them", "some", "me", "people", "take",
	"out", "into", "just", "see", "him", "your", "come", "could", "now",
	"than", "like", "other", "how", "then", "its", "our", "two", "more",
	"these", "want", "way", "look", "first", "also", "new", "because",
	"day", "more", "use", "no", "man", "find", "here", "thing", "give",
	"many", "well"]
	for word in ngram:
		if word in commonWords:
			return True
	return False
if __name__ == '__main__':
	content = str(urlopen('http://pythonscraping.com/files/inaugurationSpeech.txt').read())
	content = ngram(content,2)
	sortedNGrams = sorted(content.items(), key = operator.itemgetter(1), reverse=True)
	print sortedNGrams
	