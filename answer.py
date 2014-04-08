#!/usr/bin/env python

import sys
import nltk
import classify
import re
import evaluate

basename = sys.argv[1]
questions_fname = sys.argv[2]

questionfile = open(questions_fname,"r")
sentfile = open(basename+".sentences","r")
sentences = sentfile.read().strip().split('\n')
sentfile.close()
while '' in sentences:
  sentences.remove('')
for s in sentences:
  if s.strip()=='':
    sentences.remove(s)

# some constants
months = ['January','February','March','April','May','June','July','August','September','October','November','December']

#some helper functions
def populationDensity(sent1,sent2):
  if 'population density' in sent1:
    return sent1
  elif 'population density' in sent2:
    return sent2
  return ''

def populationSize(sent1,sent2):
  if 'population of' in sent1:
    return sent1
  elif 'population of' in sent2:
    return sent2
  elif 'inhabitants' in sent1:
    return sent1
  elif 'inhabitants' in sent2:
    return sent2
  return ''

def transportationTypes(sent1,sent2):
  common_transport = ['what','types','public','transportation','transport','transit','bus','train','rail','metro','bike','bicycle','foot','include','consist']
  count1 = 0
  for word in sent1.split():
    if word in common_transport:
      count1 += 1
  count2 = 0
  for word in sent2.split():
    if word in common_transport:
      count2 += 1
  if count1 >= 4 and count2 >=4:
    return sent1+' '+sent2
  elif count1 >=4 and count2 <4:
    return sent1
  elif count1 < 4 and count2 >=4:
    return sent2
  return ''

classification = classify.classify_article(basename)
#print classification

# here we attempt to deal with generic known-questions for the different
# types of articles
def answer_common_questions(qw,cl):
  qw = map(str.lower,qw)
  if cl=='person':

    #deal with birthday / born / etc
    #common patterns
    common_birth = ['on','what','day','date','year','when','was','did','he','she','born','birth','birthday','death','died','dead','die','come','into','this','world']
    common_birth.extend(sentences[0].split('_'))
    birth_date_sentence = sentences[1]
    
    #match 14 June 1643
    date_regex1 = r'([0-9]{1,2}.[A-Z][a-z]{1,15}.[0-9]{4})'
    dates1 = re.findall(date_regex1,birth_date_sentence)

    #match June 14, 1643
    date_regex2 = r'([A-Z][a-z]{1,15}.[0-9]{1,2},.[0-9]{4})'
    dates2 = re.findall(date_regex2,birth_date_sentence)
    
    dates = dates1 + dates2
    birth_date = dates[0]
    death_date = dates[1]
    
    matchcount = 0
    birth = False
    death = False
    for word in qw:
      if word in common_birth:
        birth = word in ['birth','born','birthday','come']
        death = word in ['death','died','dead','die']
        matchcount += 1

    #print matchcount
    if matchcount >= 4 and (birth or death):
      #print qw
      # we found birth
      if birth:
        return birth_date
      if death:
        if 'how' in qw and 'old' in qw:
          #calculate age:
          dyear = int(death_date[-5:])
          byear = int(birth_date[-5:])
          dmonth = months.index(re.findall('([A-Z][a-z]{1,15})',death_date)[0])
          bmonth = months.index(re.findall('([A-Z][a-z]{1,15})',birth_date)[0])
          
          base = dyear - byear
          if dmonth < bmonth:
            return str(base-1)
          elif dmonth > bmonth:
            return str(base)
          else: #equal, need to check date
            dday = int(re.findall('([0-9]{1,2})',death_date[:-5])[0])
            bday = int(re.findall('([0-9]{1,2})',birth_date[:-5])[0])
            if dday < bday:
              return str(base-1)
            else:
              return str(base)
        return death_date

  if cl=='city':
    
    common_population = ['what','is','population','density','size','of']
    common_population.extend(sentences[0].split('_'))
    
    matchcount = 0
    for word in qw:
      if word in common_population:
        matchcount += 1

    #deal with 'what is population density?'
    if matchcount>=3 and 'population' in qw and 'density' in qw:
      pd = reduce(populationDensity,sentences)
      return pd

    #deal with 'what is population size?'
    if matchcount >= 4:
      # possible asking for population size
      # need to check for population, inhabitants, and other stuff
      # also need to pick correct population if more than one listed
      return reduce(populationSize,sentences)

    #deal with 'types of transportation'
    common_transport = ['what','types','public','transportation','transport','transit','bus','train','rail','metro','bike','bicycle','foot']
    matchcount = 0
    for word in qw:
      if word in common_transport:
        matchcount += 1
    if matchcount >= 3:
      #check sentences for list of types of transportation
      return reduce(transportationTypes,sentences)

    return ''

  return ''


for question in questionfile:
  answer = ''
  if question.strip()=="":
    continue

  question = question.replace("?","")
  qwords = question.split()

  # first we check for common question types, based on classificaiton
  common_answer = answer_common_questions(qwords,classification)
  if not common_answer=='':
    answer = common_answer.strip()
    #afluency = evaluate.answer_score(answer)
    #print afluency
    print answer
    continue

  possibleanswers = dict()

  for sentence in sentences:
    sentence2 = sentence.lower()
    numwords = 0
    for word in qwords:
      word = word.lower()

      #if word in ['the','of','is']:
      #  continue

      word2 = ""
      word3 = ""
      if classification=='person' and word.lower() in sentences[0].lower().split('_'):
        #print "swapping out "+word+" for he/she"
        word2 = "he"
        word3 = "she"

      if word in sentence2:
        numwords += 1
      else:
        if (not(word2=='' and word3=='')) and (word2 in sentence2 or word3 in sentence2):
          #print "found he/she"
          numwords += 1

    possibleanswers[sentence] = numwords

  answer = max(possibleanswers,key=lambda k: possibleanswers[k])

  #afluency = evaluate.answer_score(answer)
  #print afluency
  print answer.strip()

questionfile.close()

