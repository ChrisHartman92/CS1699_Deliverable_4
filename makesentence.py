#!/usr/bin/env python

import nltk
import string
import nltk.data
import sys

article = sys.argv[1]
raw = open(article)
text=raw.read()
raw.close()

senttokenizer = nltk.data.load('nltk:tokenizers/punkt/english.pickle')

sentname = article + '.sentences'
sentfile = open(sentname,'w')

for line in senttokenizer.tokenize(text):
        sentfile.write(line)
        sentfile.write('\n')
sentfile.close()
