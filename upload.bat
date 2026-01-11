@echo off
REM ================================
REM GitHub Upload Script for AkashGo
REM ================================

REM Change to your project directory
cd /d "C:\Users\sohag\Downloads\AkashGO"

REM Initialize Git if not already done
IF NOT EXIST .git (
    echo Initializing new Git repository...
    git init
    git branch -M main
    git remote add origin https://github.com/sohag1192/testing.git
)

REM Create README.md only if it doesn’t exist
IF NOT EXIST README.md (
    echo # testing > README.md
)

REM Stage ALL files in the folder
git add .

REM Commit changes
git commit -m "Initial commit with all files"

REM Push to GitHub (first time with upstream)
git push origin main
git push origin main --force

