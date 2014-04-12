#!/usr/bin/env python
from __future__ import division
import en
import nltk
import pickle

questions = open('questfile')
taggedQuestions = []
for line in questions:
    tagq = en.sentence.tag(line)
    tagText = ''
    for i in range(len(tagq)):
        qtag = tagq[i][1]
        tagText += qtag[:2]+'#'
    taggedQuestions.append(tagText)
questions.close()

def question_score(quest):
    tagged = en.sentence.tag(quest)
    sample = ''
    for i in range(len(tagged)):
        tag = tagged[i][1]
        sample += tag[:2]+'#'
    fluency = 0
    minLength = 1000
    for item in taggedQuestions:
        distance = nltk.metrics.edit_distance(sample, item)
        if distance < minLength:
            minLength = distance
    fluency =  minLength
    return fluency

def answer_score(quest,answer):
  if quest in qs:
    # we have question already, so compare answer to answers
    answers = qadict[quest]
    minIndex = 0
    minDist = 1000
    for i in range(len(answers)):
      a = answers[i]
      # get the edit distance from proposed answer to existing answer
      distance = nltk.metrics.edit_distance(a,answer)
      if distance < minDist:
        minDist = distance
        minIndex = i
    # closest answer is now in answers[minIndex]
