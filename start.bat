@echo off
title Label Automation v2.0 - Quick Start

echo 🚀 Label Automation v2.0 - Quick Start
echo =======================================

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed. Please install Python 3.7+ first.
    echo    Download from: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo ✅ Python found:
python --version

REM Check if pip is available
python -m pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ pip is not available. Installing pip...
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py
    del get-pip.py
)

echo ✅ pip found:
python -m pip --version

REM Upgrade pip to latest version
echo 🔄 Upgrading pip to latest version...
python -m pip install --upgrade pip

REM Install required packages
echo 📦 Installing required packages...
python -m pip install -r requirements.txt

REM Install additional packages mentioned in README
echo 📦 Installing additional packages...
python -m pip install customtkinter tkinterdnd2 pytesseract pillow python-docx pypdf

REM Check for Tesseract OCR
echo 🔍 Checking for Tesseract OCR...
tesseract --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️  Tesseract OCR not found. OCR features for images/PDFs will not work.
    echo    Install Tesseract OCR from: https://github.com/UB-Mannheim/tesseract/wiki
    echo.
    set /p continue="Continue without Tesseract? (y/n): "
    if /i not "%continue%"=="y" exit /b 1
) else (
    echo ✅ Tesseract OCR found:
    tesseract --version | findstr "tesseract"
)

REM Run the application
echo.
echo 🎯 Starting Label Automation v2.0...
echo    If you encounter any issues, check that all dependencies are properly installed.
echo.

cd /d "%~dp0"
python src\gui.py

pause 