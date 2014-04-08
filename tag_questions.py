#!/usr/bin/env python

import nltk

f = open("raw_questions.txt","r")
contents = f.read()
f.close()

questions = contents.split("\n\n")

index = 0
arr = []

for q in questions:
  data = q.split("\n")
  arr.append(data)
  index += 1

f = open("questions_POStagged.txt","w")
for i in range(index):
  data = arr[i]
  #print data
  #if not len(data)==7:
  #  print(len(data)) 


  mystr =  str(i) + "\n"
  mystr += "Topic:"+data[1]+"\n"
  mystr += data[3]+"\n"
  text = nltk.word_tokenize(data[3])
  taglist = nltk.pos_tag(text)
  tagstr = " ".join(map(lambda x: x[1],taglist))
  mystr += tagstr + "\n"
  f.write(mystr+"\n")

f.close()

