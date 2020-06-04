@ECHO OFF
ECHO Congratulations! Your first batch file executed successfully.

for /f "tokens=1-4 delims=-/ " %%i IN ("%date%") DO (
set year=%%i
set month=%%j
set day=%%k
)

for /f "tokens=1-4 delims=:." %%i IN ("%time%") DO (
set hour=%%i
set minute=%%j
set second=%%k
rem set centisecond=%%l
)

SET OutputDir=%year%/%month%/%day%-%hour%:%minute%:%second%
ECHO %OutputDir%

rem set /p msg="Enter msg: "
git add .
rem git commit -m msg
git commit -m %OutputDir%
git push origin master

PAUSE