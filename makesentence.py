#!/usr/bin/env python

import nltk
import string
import nltk.data
import sys

article = sys.argv[1]
raw = open(article)
text=raw.read()
raw.close()

sentToken = nltk.data.load('nltk:tokenizers/punkt/english.pickle')

sentName = article + '.sentences'
sentFile = open(sentName,'w')

for line in sentToken.tokenize(text):
        sentFile.write(line)
        sentFile.write('\n')
sentFile.close()
