#!/bin/bash

# Label Automation v2.0 - Quick Start Script
# This script automatically installs dependencies and runs the application

echo "🚀 Label Automation v2.0 - Quick Start"
echo "======================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
    echo "❌ Python is not installed. Please install Python 3.7+ first."
    echo "   Download from: https://www.python.org/downloads/"
    exit 1
fi

# Use python3 if available, otherwise python
PYTHON_CMD="python3"
if ! command -v python3 &> /dev/null; then
    PYTHON_CMD="python"
fi

echo "✅ Python found: $($PYTHON_CMD --version)"

# Check if pip is available
if ! $PYTHON_CMD -m pip --version &> /dev/null; then
    echo "❌ pip is not available. Installing pip..."
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    $PYTHON_CMD get-pip.py
    rm get-pip.py
fi

echo "✅ pip found: $($PYTHON_CMD -m pip --version)"

# Upgrade pip to latest version
echo "🔄 Upgrading pip to latest version..."
$PYTHON_CMD -m pip install --upgrade pip

# Install required packages
echo "📦 Installing required packages..."
$PYTHON_CMD -m pip install -r requirements.txt

# Install additional packages mentioned in README
echo "📦 Installing additional packages..."
$PYTHON_CMD -m pip install customtkinter tkinterdnd2 pytesseract pillow python-docx pypdf

# Check for Tesseract OCR
echo "🔍 Checking for Tesseract OCR..."
if ! command -v tesseract &> /dev/null; then
    echo "⚠️  Tesseract OCR not found. OCR features for images/PDFs will not work."
    echo "   Install Tesseract OCR:"
    echo "   - macOS: brew install tesseract"
    echo "   - Ubuntu/Debian: sudo apt-get install tesseract-ocr"
    echo "   - Windows: Download from https://github.com/UB-Mannheim/tesseract/wiki"
    echo ""
    read -p "Continue without Tesseract? (y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
else
    echo "✅ Tesseract OCR found: $(tesseract --version | head -n 1)"
fi

# Run the application
echo ""
echo "🎯 Starting Label Automation v2.0..."
echo "   If you encounter any issues, check that all dependencies are properly installed."
echo ""

cd "$(dirname "$0")"
$PYTHON_CMD src/gui.py 