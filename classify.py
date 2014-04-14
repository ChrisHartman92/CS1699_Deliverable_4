#!/usr/bin/env python
import nltk
def stripAndSplit(fileContents, splitOn):
	readIt = fileContents.read()
	stripIt = readIt.strip()
	splitIt = stripIt.split(splitOn)
	return splitIt

def checkLanguage(lineList):
	if 'language' in lineList[0]:
		return True

def checkInstrument(lineList, instList):
	if lineList[0] in instList:
		return True

def checkCity(lineList, threshold):
	count = 0
	
	for line in lineList:
		currLine = nltk.word_tokenize(line)
		for token in currLine:
			if token == 'city':
				count += 1
	if count > threshold:
		return True

def classify_article(fileName):

	# list of instruments compiled from wikipedia
	instFileContents = open('instruments.txt')
	instrumentList = []
	for line in instFileContents:
		instrumentList.append(line.strip())
	instFileContents.close()

	# some constants for classifying cities
	city = 'city'
	cityThreshold=15

	doc=open(fileName,'r')

	lines = stripAndSplit(doc, '\n')
	if (checkLanguage(lines)):
		return 'language'

	if (checkInstrument(lines, instrumentList)):
		 return 'instrument'

	if (checkCity(lines, cityThreshold)):
		return 'city'

	return 'person'

