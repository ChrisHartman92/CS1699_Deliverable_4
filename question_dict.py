#!/usr/bin/env python

import sys

qtempfile = sys.argv[1]
f = open(qtempfile,'r')
nqs = f.read().strip().split('\n')
f.close()

qdict = 'question.dictionary'
f = open(qdict,'r')
qs = f.read().strip().split('\n')
f.close()

for nq in nqs:
  if nq.strip()=='':
    continue
  nq = nq.strip()
  if not nq in qs:
    qs.append(nq)

f = open(qdict,'w')
for q in qs:
  f.write(q+'\n')
f.close()

