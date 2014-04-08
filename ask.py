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
import askfunc

article = sys.argv[1]
nquestions = int(sys.argv[2])

sentname = article + '.sentences'
sentfile = open(sentname)
sentences = sentfile.read().split('\n')
sentfile.close()
cannedarray=[]
classification = 'person'

cannedarray = askfunc.getClassification(article, sentences)
askfunc.printQuests(nquestions, cannedarray)

questionarray=[]

f = open(sentname)
text=f.read()
f.seek(0)
num=0
appos = []
current = ''
record = 0
scorearray=[]
citycount=0
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
    if line[i] not in string.whitespace:
      word = askfunc.fappend(word,line[i])
      if word=='city':
        citycount+=1
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
      
      if word == 'was' and numwords<2:
        question[0] = 'Was'
      else:
        if word != 'also':
          question.append(word)
      word=''
      numwords+=1

  # post-process question
  if classification=='person':
    firstlast=sentences[0].split('_')
    if firstlast[1] not in question:
      if 'he' in question:
        question[question.index('he')]=firstlast[1]
      elif 'He' in question:
        question[question.index('He')]=firstlast[1]
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
        qstring = (qstring + question[j] + ' ')
      if '?' in question[j]:
        break

    randvar=random.random()
    vstring = askfunc.standardize(qstring)
    
    verbose = askfunc.makeVerbose(vstring)

    qtagged = nltk.pos_tag(question)                        

    inspos=-2
    for k in range(len(qtagged)):
      if qtagged[k][1] != 'NNP' and qtagged[k] != 'PRP' and inspos==-2:
        inspos = k
        negarray=list(question)
        negarray.insert(inspos,'not')
        break
    
    negquestion=''
    for item in negarray:
      negquestion+= item + ' '
      if '?' in item:
        break
    
    # add easy questions to question array
    questionarray.append(negquestion.strip())
    questionarray.append(qstring.strip())
    questionarray.append(verbose.strip())
    if replaced==1:
      qstring=''
      for j in range(len(sentence)):
        if j==len(sentence)-1:
          sentence[j]=sentence[j].replace('.','?')
        qstring = (qstring + ' '+sentence[j])
      #print qstring.strip()
      questionarray.append(qstring.strip())


for m in re.finditer("is the .{,20} of .{5,30}\.",text):
  endq=m.group(0)[:len(m.group(0))-1]
  questionarray.append('What %s?' % (endq))
f.seek(0)
'''for line in f:
  for m in re.finditer("[A-Z].{,50} is (.{,30})[/./,/;]",line):
    if re.match("[A-Z].{,50} is (.{,30})[/./,/;]",line):
      isq=m.group(0)
      isq=isq.replace(isq[0],isq[0].lower())
      isq=isq.replace(' is ',' ')
      questionarray.append('Is %s?' % (isq[0:len(isq)-1]))'''

askfunc.removeQuestions(questionarray)

for line in f:
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
      questionarray.append('What is the significance of %s?' %date)
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
      questionarray.append('What is the significance of %s?' %date)
  for m in re.finditer("in ([0-2][1-9][1-9][1-9])",line):
    if re.search("in ([0-2][1-9][1-9][1-9])",line):
      year=m.group(0)
      year=year.replace('in ','')
      year=pronounce.pronounce_year(year)
      questionarray.append('What happened in %s?' %year)

f.close()
       
for q in questionarray:
  if q.count('"')%2 !=0:
    questionarray.remove(q)
  elif q.count('(')!=q.count(')'):
    questionarray.remove(q)
if len(questionarray)==0:
  questionarray=cannedarray
while len(questionarray) < nquestions:
  questionarray.extend(questionarray)
fqs = random.sample(questionarray,nquestions)
for q in fqs:
  print q

if __name__ == "__main__":
	import sys
	ask(int(sys.argv[1],sys.argv[2]))
