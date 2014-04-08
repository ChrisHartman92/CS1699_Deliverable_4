#!/usr/bin/env python

import nltk
import string
import nltk.data
import sys

article = sys.argv[1]
textfile = article+'.txt'
raw = open(textfile)

text=raw.read()
raw.close()
senttokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
sentname = article + '.sentences'
sentfile = open(sentname,'w')
for line in senttokenizer.tokenize(text):
        sentfile.write(line)
        sentfile.write('\n')
sentfile.close()

f = open(sentname)
num=0
appos = []
current = ''
record = 0
questionarray=[]
for line in f:
	#print line
	size = len(line)
	question = []
	sentence= []
	question.append('')
	qstring = ''
	numwords=0
	word = ''
	replaced=0
	for i in range(size):
		'''if record == 1 and line[i] != ')':
			current = current + line[i]
		if line[i] == '(':
			record = 1
		else:
			if line[i] == ')':
				record = 0'''
		if line[i] not in string.whitespace:
			word = word+line[i]
		else:
                        if word.lower() == 'he' and replaced!=1:
                                sentence.append('who')
                                replaced=1
                        else:
                                sentence.append(word)
			if word == 'was' and numwords<2:
				question[0] = 'Was'
			else:
				question.append(word)
			word=''
			numwords+=1
	if question[0]=='Was':
		if question[1].lower() == 'because' and question[2].lower()=='it':
			question[2]='because'
			question[1]='it'
		quote=1
		for j in range(len(question)):
                        if '"' in question[j]:
                                quote*=-1
                        if quote == 1:
                                if ';' in question[j]:
                                        question[j]=question[j].replace(';','?')

                                else:
                                        if ',' in question[j]:
                                                question[j]=question[j].replace(',','?')
                                        else:
                                                if ':' in question[j]:
                                                        question[j]=question[j].replace(':','?')
                        if j==len(question)-1:
                                question[j]=question[j].replace('.','?')
                        qstring = (qstring + question[j] + ' ')
			if '?' in question[j]:
                                break
		print qstring
		print '\n'
		questionarray.append(qstring)
        if replaced==1:
                qstring=''
                for j in range(len(sentence)):
                        if j==len(sentence)-1:
                                sentence[j]=sentence[j].replace('.','?')
                        qstring = (qstring + ' '+sentence[j])
                #qstring = qstring + '?'
                print qstring
                print '\n'
'''
        tokened = nltk.word_tokenize(line)
        tagged = nltk.pos_tag(tokened)
        #print tagged
        pflag=-1
        found=0
        phrase=''
        for i in range(len(tagged)):
                if tagged[i][1]=='IN':
                        found=0
                        pflag*=-1
                        if pflag==1:
                                start=i
                        else:
                                end=i
                                found=1
                                for j in range(start+1,end):
                                        phrase=(phrase+' '+tagged[j][0])
                                break
        if found==1:
                print phrase
                line=line.replace(phrase, ' what')
                print line
                
                        

#for i in range(len(appos)):
#	print appos[i]

	
'''

