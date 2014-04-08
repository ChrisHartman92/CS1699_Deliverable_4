#!/bin/sh

article=$1
nquestions=$2

./makesentence.py $article

./ask.py $article $nquestions > temp.$$.txt

#python question_dict.py temp.$$.txt

cat temp.$$.txt

rm temp.$$.txt

