@ECHO OFF
ECHO Congratulations! Your first batch file executed successfully.

set /p msg="Enter msg: "
git add .
git commit -m msg
git push origin master

PAUSE