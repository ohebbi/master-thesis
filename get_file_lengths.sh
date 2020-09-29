#!/bin/bash


echo "* -diff" >> .gitattributes

outfile=./lengths.txt

> $outfile

for f in $(ls *.tex); do
    git log --stat $f >> $outfile;
done

sed -i "" '$d' .gitattributes
