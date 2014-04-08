#!/usr/bin/env python

import sys
import pickle

questionFile = sys.argv[1]
answerFile = sys.argv[2]

questAnsDict = dict()

questAnsFile = open('qa.dictionary','r')
questAnsDict = pickle.load(questAnsFile)
questAnsFile.close()

questFileContents = getFileContents(questionfile)
ansFileContents = getFileContents(answerfile)

questions = stripAndSplit(questFileContents, '\n')
answers = stripAndSplit(ansFileContents, '\n')

questAnsLength = len(questions)

questAnsDict = eliminateRepeats(questions, answers, questAnsDict, questAnsLength)

questAnsFile = open('qa.dictionary','w')
pickle.dump(questAnsDict,questAnsFile)
questAndFile.close()


#This allows us to test if getting a file's contents has worked before we try to use the contents of the file for anything
def getFileContents(fileToOpen):
  tempFile = open(fileToOpen, 'r')
  return fileToOpen

#This used to be done all at once, which violated the Law of Demeter. Now it is seperate, which allows us to test each step
#Also allows us to now pass in different values to split on
def stripAndSplit(fileContents, splitOn):
  readIt = fileContents.read()
  stripIt = readIt.strip()
  splitIt = stripIt.split(splitOn)
  return splitIt

#It was not clear what this code did before, but now that it is labeled and the variable names are changed, it is more clear.
#In addition, because it returns a value, we can test it more easily
def eliminateRepeats(quests, ans, qADict, qADictLength):
  for i in range(qADictLength):
    q = quests[i]
    a = ans[i]

    if not q in qADict:
      qADict[q] = []

    if not a in qADict:
      qADict[q].append(a) 

  return qADict
