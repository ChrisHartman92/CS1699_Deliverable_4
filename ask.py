#!/usr/bin/env python
from __future__ import division
import nltk
import string
import nltk.data
import sys
import random
import re
import classify
import pronounce
import evaluate

'Moved code from askfunc.py to satisfy the single responsibility principle. Ask now encapsualtes all of ask and its functions.'

#Input: sentence file
#Output: Array with appropriate canned questions
#Notes: These questions apply to the category person

def personQuest(sentences):
 cannedArray=[]
 cannedArray.append('On what date was %s born?' % sentences[0].replace('_',' '))
 cannedArray.append('On what date did %s die?' % sentences[0].replace('_',' '))
 cannedArray.append('How old was %s when he died?' % sentences[0].replace('_',' '))
 cannedArray.append('Was %s ever married?' % sentences[0].replace('_',' '))
 cannedArray.append('Who was %s?' % sentences[0].replace('_',' '))
 cannedArray.append('Did %s attend college?' % sentences[0].replace('_',' '))
 cannedArray.append('When did %s come into this world?' % sentences[0].replace('_',' '))
 cannedArray.append('Does the article mention that %s published anything?' % sentences[0].replace('_',' '))
 return cannedArray

#Input: sentence file
#Output: Array with appropriate canned questions
#Notes: These questions apply to the category language

def languageQuest(sentences): 
 cannedArray=[]
 cannedArray.append('Where is the %s spoken?' % sentences[0].replace('_',' '))
 cannedArray.append('What language family is the %s a part of?' % sentences[0].replace('_',' '))
 cannedArray.append('Approximately how many people speak the %s?' % sentences[0].replace('_',' '))
 cannedArray.append('Who speaks the %s?' % sentences[0].replace('_',' '))
 cannedArray.append('What is the word order in %s?' % sentences[0].replace('_',' '))
 cannedArray.append('Does the %s have vowels?' % sentences[0].replace('_',' '))
 cannedArray.append('How many vowels does %s have?' % sentences[0].replace('_',' '))
 return cannedArray

#Input: sentence file
#Output: Array with appropriate canned questions
#Notes: These questions apply to the category city

def cityQuest(sentences):
 cannedArray=[]
 cannedArray.append('What is the population of %s?' % sentences[0].replace('_',' '))
 cannedArray.append('In what country is %s?' % sentences[0].replace('_',' '))
 cannedArray.append('What is the population density of %s?' % sentences[0].replace('_',' '))
 cannedArray.append('What kind of transportation exists in %s?' % sentences[0].replace('_',' '))
 cannedArray.append('Where is %s?' % sentences[0].replace('_',' '))
 cannedArray.append('How old is %s?' % sentences[0].replace('_',' '))
 cannedArray.append('What kind of climate does %s have?' % sentences[0].replace('_',' '))
 return cannedArray

#Input: sentence file
#Output: Array with appropriate canned questions
#Notes: These questions apply to the category instrument

def instrumentQuest(sentences):
 cannedArray=[]
 cannedArray.append('What is the %s?' % sentences[0].replace('_',' '))
 cannedArray.append('How is the %s played?' % sentences[0].replace('_',' '))
 cannedArray.append('How does one play the %s?' % sentences[0].replace('_',' '))
 cannedArray.append('Does the %s have strings?' % sentences[0].replace('_',' '))
 cannedArray.append('Is the %s a wind instrument?' % sentences[0].replace('_',' '))
 cannedArray.append('Is the %s a percussion instrument?' % sentences[0].replace('_',' '))
 cannedArray.append('Where does the %s originate?' % sentences[0].replace('_',' '))
 cannedArray.append('What kind of music is played on the %s?' % sentences[0].replace('_',' '))
 return cannedArray

#Input: article file, sentence file
#Output: Array with the appropraite canned questions
#Notes: On return calls personQuest, languageQuest, cityQuest, or intrumentQuest

def getClassification(article, sentences):
 classification=classify.classify_article(article)
 if classification == 'person':
	return personQuest(sentences)
 elif classification == 'language':
	return languageQuest(sentences)
 elif classification == 'city':
	return cityQuest(sentences)
 elif classification == 'instrument':
	return instrumentQuest(sentences)

#Input: two strings, a base and an item
#Output: The two input strings combined, with the item appended on to the end of the base

def fappend(base,item) :
	base+=item
	return base

#Input: int for the number of questions to print, an array of questions
#Ouput: cannedArray[0] - number of questions

def printQuests(numberOfQuestions,cannedArray) :
	returnArray = []
	for i in range(1,numberOfQuestions) :
		print cannedArray[i-1]
		returnArray.append(cannedArray[i-1])
		if i == len(cannedArray) :
			numberOfQuestions = numberOfQuestions - i
			break;
	return returnArray

#Input: String to be made verbose
#Output: String with verbose prefix attached

def makeVerbose(verboseString):
	verbose='According to the information given in the article, '+verboseString
	return verbose

#Input: array of questions
#Output: removes appropriate questions

def removeQuestions(questionArray):
	for q in questionArray:
		if re.search(r"\(.*who.*\)",q):
			questionArray.remove(q)
			continue
		tokened = tokenize(q)
		b = shouldCompare(tokened)
		if b:
			fluency = getFluency(q)
			if fluency>6:
				questionArray.remove(q)

#Input: tokened string
#Output: boolean representing whether the string should be compared

def shouldCompare(tokened):
	return len(tokened)<10

#Input: string to be tokenized
#Output: tokenized string

def tokenize(q):
	return nltk.word_tokenize(q)

#Input: string to evaluate
#Ouput: fluency of input string

def getFluency(q) :
	a = evaluate.question_score(q)
	return a

#Input: Verbose string
#Ouput: Standerdized (lower case) verbose string

def standardize(verboseString):
	verboseString = verboseString.strip()
	verboseString = verboseString.replace(verboseString[0],verboseString[0].lower())
	return verboseString

#Input: contents of file, string to split on
#Output: contents of file stripped and split on input string

def stripAndSplit(fileContents, splitOn):
	readIt = fileContents.read()
	stripIt = readIt.strip()
	splitIt = stripIt.split(splitOn)
	return splitIt

if __name__ == "__main__":
	import sys
	ask(int(sys.argv[1],sys.argv[2]))

#article = sys.argv[1]
article = "city_text.txt" 
#numberOfQuestions = int(sys.argv[2])
numberOfQuestions = 5 

sentenceName = article + '.sentences'
sentenceFile = open(sentenceName)
sentences = stripAndSplit(sentenceFile, '\n')
sentenceFile.close()
cannedArray=[]
classification = 'person'

cannedArray = getClassification(article, sentences)
printQuests(numberOfQuestions, cannedArray)

questionArray=[]

fileData = open(sentenceName)
text=fileData.read()
fileData.seek(0)
num=0
appos = []
current = ''
record = 0
scoreArray=[]
cityCount=0
for line in fileData:
	#print line
	size = len(line)
	question = []
	sentence= []
	question.append('')
	questionString = ''
	numberOfWords=0
	word = ''
	replaced=0
	for i in range(size):
		if line[i] not in string.whitespace:
			word = fappend(word,line[i])
			if word=='city':
				cityCount+=1
		else:
			if word.lower() == 'he' and replaced!=1:
				if word == 'he':
					sentence.append('who')
				else:
					sentence.append('Who')
				replaced=1
			else:
				if word != 'also':
					sentence.append(word)
			
			if word == 'was' and numberOfWords<2:
				question[0] = 'Was'
			else:
				if word != 'also':
					question.append(word)
			word=''
			numberOfWords+=1

	# post-process question
	if classification=='person':
		firstLast=sentences[0].split('_')
		if firstLast not in question:
			if 'he' in question:
				question[question.index('he')]=firstLast[1]
			elif 'He' in question:
				question[question.index('He')]=firstLast[1]
	if question[0]=='Was':
		if question[1].lower() == 'because' and question[2].lower()=='it':
			question[2]='because'
			question[1]='it'
		if question[1] not in sentences[0]:
			question[1]=question[1].lower() #fixes incorrect capitalization problem
		quote=1
		for j in range(len(question)):
			if '"' in question[j]:
				quote*=-1
			if quote == 1:
				if ';' in question[j]:
					question[j]=question[j].replace(';','?')
				elif ',' in question[j]:
					question[j]=question[j].replace(',','?')
				elif ':' in question[j]:
					question[j]=question[j].replace(':','?')
				if j==len(question)-1:
					question[j]=question[j].replace('.','?')
				questionString = (questionString + question[j] + ' ')
			if '?' in question[j]:
				break

		randVar=random.random()
		verboseString = standardize(questionString)
		
		verbose = makeVerbose(verboseString)

		taggedQuestion = nltk.pos_tag(question)												

		sentPosition=-2
		for k in range(len(taggedQuestion)):
			if taggedQuestion[k][1] != 'NNP' and taggedQuestion[k] != 'PRP' and sentPosition==-2:
				sentPosition = k
				negArray=list(question)
				negArray.insert(sentPosition,'not')
				break
		
		negQuestion=''
		for item in negArray:
			negQuestion+= item + ' '
			if '?' in item:
				break
		
		# add easy questions to question array
		questionArray.append(negQuestion.strip())
		questionArray.append(questionString.strip())
		questionArray.append(verbose.strip())
		if replaced==1:
			questionString=''
			for j in range(len(sentence)):
				if j==len(sentence)-1:
					sentence[j]=sentence[j].replace('.','?')
				questionString = (questionString + ' '+sentence[j])
			#print questionString.strip()
			questionArray.append(questionString.strip())


for m in re.finditer("is the .{,20} of .{5,30}\.",text):
	endq=m.group(0)[:len(m.group(0))-1]
	questionArray.append('What %s?' % (endq))
fileData.seek(0)

removeQuestions(questionArray)

for line in fileData:
	for m in re.finditer("[1-2]{0,1}[0-9]\s((January)|(February)|(March)|(April)|(May)|(June)|(July)|(August)|(September)|(October)|(November)|(December))\s([0-2][0-9][0-9][0-9])",line):
		if re.search("[1-2]{0,1}[0-9]\s((January)|(February)|(March)|(April)|(May)|(June)|(July)|(August)|(September)|(October)|(November)|(December))\s([0-2][0-9][0-9][0-9])",line):
			date=m.group(0)
			year=date[-4:]
			year=pronounce.pronounce_year(year)
			if re.match("[10-31]",date):
				day=date[:2]
				day='the '+pronounce.pronounce_day(day).lower()+' of'
				date=day+date[2:]
			else:
				day=date[0]
				day='the '+pronounce.pronounce_day(day)+' of'
				date=day+date[1:]
			day='the '+pronounce.pronounce_day(day)+' of'
			date=date[:-4]+year
			questionArray.append('What is the significance of %s?' %date)
	for m in re.finditer("((January)|(February)|(March)|(April)|(May)|(June)|(July)|(August)|(September)|(October)|(November)|(December)) [0-9]{1,2}, ([0-2][0-9][0-9][0-9])",line):
		if re.search("((January)|(February)|(March)|(April)|(May)|(June)|(July)|(August)|(September)|(October)|(November)|(December)) [0-9]{1,2}, ([0-2][0-9][0-9][0-9])",line):
			date=m.group(0)
			year=date[-4:]
			year=pronounce.pronounce_year(year)
			if re.match("[10-31]",date[-8:-6]):
				day=date[-8:-6]
				day=pronounce.pronounce_day(day).lower()
				date=date[:-8]+day+date[-6:]
			else:
				day=date[-7]
				day=pronounce.pronounce_day(day).lower()
				date=date[:-7]+day+date[-6:]
			date=date[:-4]+year
			questionArray.append('What is the significance of %s?' %date)
	for m in re.finditer("in ([0-2][1-9][1-9][1-9])",line):
		if re.search("in ([0-2][1-9][1-9][1-9])",line):
			year=m.group(0)
			year=year.replace('in ','')
			year=pronounce.pronounce_year(year)
			questionArray.append('What happened in %s?' %year)

fileData.close()
			 
for q in questionArray:
	if q.count('"')%2 !=0:
		questionArray.remove(q)
	elif q.count('(')!=q.count(')'):
		questionArray.remove(q)
if len(questionArray)==0:
	questionArray=cannedArray
while len(questionArray) < numberOfQuestions:
	questionArray.extend(questionArray)
fqs = random.sample(questionArray,numberOfQuestions)
for q in fqs:
	print q

