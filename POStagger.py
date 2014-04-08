#!/usr/bin/env python

import nltk
import string
import nltk.data
import sys

filename=sys.argv[1]
infpt = filename+'.txt'
tags = filename+'.tgs'
sents = filename + '.sentences'

f = open(infpt)
text=f.read()
f.close()
tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
stokentext=tokenizer.tokenize(text.strip())

g=open(sents,"w")
h=open(tags,"w")
for line in stokentext:
    wtokentext = nltk.word_tokenize(line)
    taggedtext = nltk.pos_tag(wtokentext)
    for item in taggedtext:
        h.write(str(item[1])+' ')
        g.write(str(item[0])+' ')
    g.write('\n')
    h.write('\n')
g.close()
h.close()
