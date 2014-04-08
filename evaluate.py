#!/usr/bin/env python
from __future__ import division
import en
import nltk
import pickle

questions=open('questfile')
taggedquestions=[]
for line in questions:
    tagq=en.sentence.tag(line)
    tagtext=''
    for i in range(len(tagq)):
        qtag=tagq[i][1]
        tagtext+=qtag[:2]+'#'
    taggedquestions.append(tagtext)
questions.close()

def question_score(quest):
    tagged=en.sentence.tag(quest)
    sample=''
    for i in range(len(tagged)):
        tag=tagged[i][1]
        sample+=tag[:2]+'#'
    fluency=0
    minlen=1000
    for item in taggedquestions:
        distance=nltk.metrics.edit_distance(sample, item)
        if distance<minlen:
            minlen=distance
    fluency= minlen
    return fluency

def answer_score(quest,answer):
  if quest in qs:
    # we have question already, so compare answer to answers
    answers = qadict[quest]
    minindex = 0
    mindist = 1000
    for i in range(len(answers)):
      a = answers[i]
      # get the edit distance from proposed answer to existing answer
      distance=nltk.metrics.edit_distance(a,answer)
      if distance<mindist:
        mindist = distance
        minindex = i
    # closest answer is now in answers[minindex]
