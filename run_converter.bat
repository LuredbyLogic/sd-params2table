@echo off
title sd-params2table

:: Clear the screen
cls

:: Prompt the user to provide the source file path
echo Please drag and drop your params .txt file onto this window, then press Enter.
echo.
set /p inputFile="Source File: "

:: Check if the user actually provided a file
if not defined inputFile (
    echo.
    echo No file was provided. Exiting.
    pause
    goto :eof
)

echo.
echo Processing file...
echo.

:: Run the python script and pass the user's input file path as an argument.
:: The "%~1" in python is replaced by the quoted path in "%inputFile%".
python param-convert.py %inputFile%

echo.
echo ---
echo Process finished.
pause