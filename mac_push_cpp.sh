#!/bin/sh

echo "============ Change directory	============"
cd /Users/howarder3/Documents/GitHub/leetcode_practice 

echo "============ Copying files	============"
cp -R /Users/howarder3/.leetcode_cpp/ /Users/howarder3/Documents/GitHub/leetcode_practice/new_practice_cpp 

# echo "============ Current datetime ============"
datetime=$(date '+%Y/%m/%d-%H:%M:%S');
echo "Current datetime: $datetime"

echo "============ Update to GitHub	============"
git pull
git add .
git commit -m $datetime
git push origin master