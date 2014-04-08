#!/bin/sh

article=$1
questions=$2

./makesentence.py $article

tempfile=temp.$$.txt

./answer.py $article $questions > $tempfile

#python qa_dictionary.py $questions $tempfile

cat $tempfile

rm $tempfile

rm $article.sentences
