#!/bin/bash


echo "* -diff" >> .gitattributes

outfile=./lengths.txt

> $outfile

for f in $(ls *.tex) or $(ls conclusion/*.tex) or $(ls methodology*implementations/*.tex) or $(ls miscellaneous/**/*.tex) or  $(ls results/*.tex) or $(ls theory/*.tex); do
    git log --date=format:'%m%d%Y' --stat $f >> $outfile;
done

sed -i "" '$d' .gitattributes
