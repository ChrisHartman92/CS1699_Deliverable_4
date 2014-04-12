#!/usr/bin/env python

import nltk
import string
import nltk.data
import sys

fileName=sys.argv[1]
textFile = fileName+'.txt'
tags = fileName+'.tgs'
sents = fileName + '.sentences'

textContents = open(textFile)
text = textContents.read()
textContents.close()
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
strippedToken = tokenizer.tokenize(text.strip())

sentContents = open(sents,"w")
tagContents = open(tags,"w")
for line in strippedToken:
    wordToken = nltk.word_tokenize(line)
    taggedText = nltk.pos_tag(wordToken)
    for item in taggedText:
        tagContents.write(str(item[1])+' ')
        sentContents.write(str(item[0])+' ')
    sentContents.write('\n')
    tagContents.write('\n')
sentContents.close()
tagContents.close()
