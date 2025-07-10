#!/usr/bin/env python3
"""
Label Automation v2.0 - Quick Start Script (Python)
This script automatically installs dependencies and runs the application
"""

import subprocess
import sys
import os
import shutil

def run_command(cmd, check=True):
    """Run a command and return the result"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=check)
        return result.returncode == 0, result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        return False, e.stdout, e.stderr

def check_python():
    """Check if Python is available and get version"""
    print("✅ Python found:", sys.version.split()[0])
    return True

def install_packages():
    """Install required packages"""
    packages = [
        "customtkinter",
        "tkinterdnd2", 
        "pytesseract",
        "pillow",
        "python-docx",
        "pypdf"
    ]
    
    print("🔄 Upgrading pip to latest version...")
    success, _, _ = run_command(f"{sys.executable} -m pip install --upgrade pip")
    
    print("📦 Installing required packages...")
    
    # Install from requirements.txt first
    if os.path.exists("requirements.txt"):
        success, _, _ = run_command(f"{sys.executable} -m pip install -r requirements.txt")
    
    # Install additional packages to ensure we have everything
    for package in packages:
        print(f"   Installing {package}...")
        success, _, stderr = run_command(f"{sys.executable} -m pip install {package}", check=False)
        if not success:
            print(f"⚠️  Warning: Could not install {package}: {stderr}")

def check_tesseract():
    """Check if Tesseract OCR is available"""
    print("🔍 Checking for Tesseract OCR...")
    
    if shutil.which("tesseract"):
        success, stdout, _ = run_command("tesseract --version", check=False)
        if success:
            version_line = stdout.split('\n')[0]
            print(f"✅ Tesseract OCR found: {version_line}")
            return True
    
    print("⚠️  Tesseract OCR not found. OCR features for images/PDFs will not work.")
    print("   Install Tesseract OCR:")
    print("   - macOS: brew install tesseract")
    print("   - Ubuntu/Debian: sudo apt-get install tesseract-ocr")
    print("   - Windows: Download from https://github.com/UB-Mannheim/tesseract/wiki")
    print()
    
    response = input("Continue without Tesseract? (y/n): ").lower().strip()
    return response in ['y', 'yes']

def run_application():
    """Run the main application"""
    print()
    print("🎯 Starting Label Automation v2.0...")
    print("   If you encounter any issues, check that all dependencies are properly installed.")
    print()
    
    # Change to script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Run the GUI application
    gui_path = os.path.join("src", "gui.py")
    if os.path.exists(gui_path):
        subprocess.run([sys.executable, gui_path])
    else:
        print(f"❌ Could not find {gui_path}")
        return False
    
    return True

def main():
    """Main startup function"""
    print("🚀 Label Automation v2.0 - Quick Start")
    print("=======================================")
    
    # Check Python
    if not check_python():
        print("❌ Python check failed")
        return False
    
    # Install packages
    install_packages()
    
    # Check Tesseract (optional)
    if not check_tesseract():
        return False
    
    # Run application
    return run_application()

if __name__ == "__main__":
    try:
        success = main()
        if not success:
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n❌ Startup cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1) 