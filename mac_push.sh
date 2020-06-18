#!/bin/sh

cd /Users/howarder3/Documents/GitHub/leetcode_practice 
cp -R /Users/howarder3/.leetcode/ /Users/howarder3/Documents/GitHub/leetcode_practice/new_practice 

datetime=$(date '+%Y/%m/%d-%H:%M:%S');
echo "$datetime"

git add .
git commit -m $datetime
git push origin master