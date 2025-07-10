# 🚀 Quick Start Guide

## Get Label Automation v2.0 Running in 30 Seconds

### Step 1: Choose Your Method

#### ✅ **EASIEST: Automatic Setup (Recommended)**
Just run one of these commands in your terminal:

- **Mac/Linux**: `./start.sh`
- **Windows**: Double-click `start.bat` 
- **Any Platform**: `python start.py`

That's it! The script will:
- ✅ Check your Python installation
- ✅ Install all required packages automatically
- ✅ Check for Tesseract OCR (optional for image/PDF scanning)
- ✅ Launch the application

#### 🔧 **Manual Setup** (if you prefer control)
```bash
# Install dependencies
pip install -r requirements.txt
pip install customtkinter tkinterdnd2 pytesseract pillow python-docx pypdf

# Run the app
python src/gui.py
```

### Step 2: Start Scanning!
1. **Drag and drop** a folder into the app, or click "Browse" to select one
2. Click **"Start Scan"** 
3. Watch as files are analyzed for sensitivity levels
4. Review results showing **Confidential**, **PII**, or **Public** classifications

### Troubleshooting

**Error: "No module named 'customtkinter'"**
- Solution: Run the automatic setup script (`./start.sh`, `start.bat`, or `python start.py`)

**OCR not working for images/PDFs:**
- Install Tesseract OCR:
  - **Mac**: `brew install tesseract`
  - **Windows**: [Download installer](https://github.com/UB-Mannheim/tesseract/wiki)
  - **Linux**: `sudo apt-get install tesseract-ocr`

**Can't run shell script:**
- Mac/Linux: Run `chmod +x start.sh` first
- Or use the Python version: `python start.py`

### What's Next?
- Customize sensitivity rules in `config/rules.json`
- Try scanning different file types (.txt, .docx, .pdf, images)
- Package as standalone executable with PyInstaller

---
**Need help?** Check the main README.md for detailed documentation. 