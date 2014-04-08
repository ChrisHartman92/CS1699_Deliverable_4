#!/usr/bin/env python
import nltk

def classify_article(filename):

  # list of instruments compiled from wikipedia
  instlist = open('instruments.txt')
  instrumentlist = []
  for line in instlist:
    instrumentlist.append(line.strip())
  instlist.close()
  
  # some constants for classifying cities
  city = 'city'
  citythreshold=15
  
  doc=open(filename,'r')
  
  lines=doc.read().strip().split('\n')
 
  if 'language' in lines[0]:
    return 'language'

  if lines[0] in instrumentlist:
    return 'instrument'

  count=0

  for l in lines:
    line=nltk.word_tokenize(l)
    for token in line:
      if token == 'city':
        count+=1

  if count>citythreshold:
      return 'city'

  return 'person'

