#!/usr/bin/env python
import nltk

def classify_article(fileName):

  # list of instruments compiled from wikipedia
  instFileContents = open('instruments.txt')
  instrumentlist = []
  for line in instFileContents:
    instrumentlist.append(line.strip())
  instFileContents.close()
  
  # some constants for classifying cities
  city = 'city'
  cityThreshold=15
  
  doc=open(fileName,'r')
  
  lines = stripAndSplit(doc, '\n')
 
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

  if count>cityThreshold:
      return 'city'

  return 'person'


def stripAndSplit(fileContents, splitOn):
  readIt = fileContents.read()
  stripIt = readIt.strip()
  splitIt = stripIt.split(splitOn)
  return splitIt
