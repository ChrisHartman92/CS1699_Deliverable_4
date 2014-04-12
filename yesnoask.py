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
sentToken = nltk.data.load('tokenizers/punkt/english.pickle')
sentName = article + '.sentences'
sentFile = open(sentName,'w')
for line in sentToken.tokenize(text):
        sentFile.write(line)
        sentFile.write('\n')
sentFile.close()

sentContents = open(sentName)
num=0
appos = []
current = ''
record = 0
questionArray=[]
for line in sentContents:
  size = len(line)
  question = []
  sentence= []
  question.append('')
  qstring = ''
  numwords=0
  word = ''
  replaced=0
  for i in range(size):
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
    questionArray.append(qstring)
  if replaced==1:
    qstring=''
  for j in range(len(sentence)):
    if j==len(sentence)-1:
      sentence[j]=sentence[j].replace('.','?')
  qstring = (qstring + ' '+sentence[j])
  print qstring
  print '\n'
