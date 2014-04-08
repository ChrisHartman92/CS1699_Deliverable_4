#!/usr/bin/env python

import sys
argFile = sys.argv[1]
questFile = open(argFile,'r')
numQuestions = stripAndSplit(questFile, '\n')
questFile.close()

questFile = open('question.dictionary','r')

questions = stripAndSplit(f, '\n')

questFile.close()

for quests in numQuestions:
  if quests.strip()=='':
    continue
  quests = quests.strip()
  if not quests in questions:
    questions.append(quests)

questFile = open('question.dictionary','w')
for quests in questions:
  questFile.write(quests+'\n')
questFile.close()

#allows us to check to make sure that file contents were stripped and split as expected.
#also allows us to split on different keywords or characters in the future if needed
def stripAndSplit(fileContents, splitOn):
  readIt = fileContents.read()
  stripIt = readIt.strip()
  splitIt = stripIt.split(splitOn)
  return splitIt
