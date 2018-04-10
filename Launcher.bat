@ECHO OFF
set /P PPYTHON_PATH=<PPYTHON_PATH
if exist FirstTimeSetup.bat (
goto A )
:A
start README.txt
set didread="n" 
SET /P didread="did you read README: (Y or N)"
echo %didread%
echo is "%didread%"
IF /I "%didread%"=="y" goto Y
goto A

:Y
echo hi
%PPYTHON_PATH% launcher.py
pause