@echo off
REM ================================
REM GitHub Upload Script for AkashGo
REM ================================

REM Change to your project directory
cd /d "C:\Users\sohag\Downloads\testing"

REM Initialize Git if not already done
IF NOT EXIST .git (
    echo Initializing new Git repository...
    git init
    git branch -M main
    git remote add origin https://github.com/sohag1192/testing.git
)


REM Stage ALL files in the folder
git add .

REM Commit changes
git commit -m "Automated commit via batch file"

REM Push to GitHub
git push -u origin main

pause

