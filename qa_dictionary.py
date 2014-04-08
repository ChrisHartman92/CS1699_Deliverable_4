#!/usr/bin/env python

import sys
import pickle

questionfile = sys.argv[1]
answerfile = sys.argv[2]

qadict = dict()

qafile = open('qa.dictionary','r')
qadict = pickle.load(qafile)
qafile.close()

qf = open(questionfile,'r')
af = open(answerfile,'r')

questions = qf.read().strip().split('\n')
answers = af.read().strip().split('\n')

qalen = len(questions)

for i in range(qalen):
  q = questions[i]
  a = answers[i]

  if not q in qadict:
    qadict[q] = []
  
  if not a in qadict[q]:
    qadict[q].append(a)

qafile = open('qa.dictionary','w')
pickle.dump(qadict,qafile)
qafile.close()

#print qadict
